# app/routes/api/v1/chat.py

from flask import request, Blueprint, jsonify


import openai
from app import cache, db
from app.models import (
    ChatSystemMessageModel,
    HelpContextModel,
    ChatHistoryModel,
    ChatMessageModel,
)

chat_api_v1 = Blueprint("chat_api_v1", __name__)

INITIALIZATION_MESSAGE_TITLE = "Initialization"
HELP_CONTEXT_MESSAGE_TITLE = "Help Context Message"
PAGE_CONTENT_MESSAGE_TITLE = "Page Content Message"
SYSTEM_GREETING_MESSAGE_TITLE = "System Greeting Message"


async def init_message_queue():
    # Fetch the cached instructional message or retrieve from DB if not cached
    initialization_message = ChatSystemMessageModel.query.filter_by(
        title=INITIALIZATION_MESSAGE_TITLE
    ).first()

    messages = [{"role": "system", "content": initialization_message.content}]

    # Help context id is used to query the system message table for additional context information
    if request.is_json and "help_context_id" in request.json:
        help_context_id = request.json.get("help_context_id")

    if help_context_id:
        help_context_message = ChatSystemMessageModel.query.filter_by(
            title=HELP_CONTEXT_MESSAGE_TITLE
        ).first()

    if help_context_message:
        help_context = HelpContextModel.query.filter_by(
            context_id=help_context_id
        ).first()

    if help_context:
        messages.append(
            {
                "role": "system",
                "content": f"{help_context_message.content}: {help_context.content}",
            }
        )

    if request.is_json and "page_content" in request.json:
        # Retrieve context from the request body
        page_content_message = ChatSystemMessageModel.query.filter_by(
            title=PAGE_CONTENT_MESSAGE_TITLE
        ).first()

    if page_content_message:
        page_content = request.json.get("page_content")

    if page_content:
        messages.append(
            {
                "role": "system",
                "content": f"{page_content_message.content}: {page_content}",
            }
        )

    return messages


async def send_messages(messages, openai_model="gpt-3.5-turbo"):
    # Check the current temperature
    if "temperature" in request.json:
        temperature = request.json["temperature"]
    else:
        temperature = 0.9

    # Send the messages to OpenAI
    openai_response = openai.ChatCompletion.create(
        model=openai_model, messages=messages, temperature=temperature
    )

    ai_message = openai_response.choices[0].message["content"].strip()

    # Create and add the AI's response to the chat history
    ai_msg_instance = ChatMessageModel(
        role=ChatMessageModel.ASSISTANT, content=ai_message
    )
    await db.async_session.add(ai_msg_instance)

    return ai_msg_instance


@chat_api_v1.route("/new", methods=["POST"])
async def new_conversation():
    chat_history = ChatHistoryModel()
    await db.async_session.add(chat_history)

    messages = init_message_queue()

    greeting = ChatSystemMessageModel.query.filter_by(
        title=SYSTEM_GREETING_MESSAGE_TITLE
    ).first()

    # Append instructions to the AI to greet the user
    messages.append(
        {
            "role": "system",
            "content": greeting.content,
        }
    )

    ai_msg_instance = send_messages(messages)

    chat_history.add_message(ai_msg_instance)
    await db.async_session.commit()

    # Select the last 20 messages from the chat history
    return (
        jsonify(
            {
                "conversation_id": chat_history.id,
                "messages": chat_history.to_dict()["messages"][-20:],
            }
        ),
        201,
    )


@chat_api_v1.route("/instructions", methods=["POST"])
async def send_instructions():
    # This endpoint is used to send specific instructions to the assistant
    # It uses a more advanced model, and provides more comprehensive instructions
    # than the chat interface
    if not request.is_json:
        return jsonify({"error": "Request mimetype must be application/json"}), 400

    if "system_message_title" in request.json:
        system_message_title = request.json.get("system_message_title")

    if not system_message_title:
        return jsonify({"error": "System message title is required"}), 400

    messages = init_message_queue()

    system_message = ChatSystemMessageModel.query.filter_by(
        title=system_message_title
    ).first()

    if not system_message:
        return jsonify(
            {
                "messages": [
                    {
                        "role": "assistant",
                        "content": f"Sorry, I was unable to complete the request. I do not understand the instruction, '{system_message_title}'.",
                    }
                ]
            }
        )

    messages.append(
        {
            "role": "system",
            "content": system_message.content,
        }
    )

    ai_msg_instance = send_messages(messages, openai_model="gpt-4")

    chat_history = ChatHistoryModel()
    await db.async_session.add(chat_history)

    chat_history.add_message(ai_msg_instance)
    await db.async_session.commit()

    return jsonify(
        {
            "id": chat_history.id,
            "messages": [
                {
                    "role": "assistant",
                    "content": ai_msg_instance.content,
                }
            ],
        }
    )


@chat_api_v1.route("/<int:conversation_id>", methods=["GET"])
async def get_conversation(conversation_id):
    chat_history = ChatHistoryModel.query.get(conversation_id)
    if chat_history is None:
        return jsonify({"error": "Conversation not found"}), 404
    return jsonify(chat_history.to_dict())


@chat_api_v1.route("/", methods=["POST"])
@chat_api_v1.route("/<int:conversation_id>", methods=["POST"])
async def send_message(conversation_id=None):
    if not request.is_json:
        return jsonify({"error": "Request mimetype must be application/json"}), 400

    if not "content" in request.json:
        return jsonify({"error": "Message content is required"}), 400

    user_message = request.json.get("content")

    chat_history = None
    if conversation_id:
        chat_history = ChatHistoryModel.query.get(conversation_id)
        if chat_history is None:
            return jsonify({"error": "Conversation not found"}), 404

    messages = init_message_queue()

    # If no conversation_id is provided, create a new ChatHistoryModel
    if chat_history:
        # Extract the last 20 messages and append to messages list
        for msg in chat_history.messages[-20:]:
            messages.append({"role": msg.role, "content": msg.content})
    else:
        chat_history = ChatHistoryModel()
        await db.async_session.add(chat_history)

    # Create and add the user's message to the chat history
    user_msg_instance = ChatMessageModel(
        role=ChatMessageModel.USER, content=user_message
    )
    await db.async_session.add(user_msg_instance)

    chat_history.add_message(user_msg_instance)

    # Add the current user message
    messages.append({"role": "user", "content": user_message})

    # Check the current temperature
    if "temperature" in request.json:
        temperature = request.json["temperature"]
    else:
        temperature = 0.9

    # Send the messages to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=temperature
    )

    ai_message = response.choices[0].message["content"].strip()

    # Create and add the AI's response to the chat history
    ai_msg_instance = ChatMessageModel(
        role=ChatMessageModel.ASSISTANT, content=ai_message
    )
    await db.async_session.add(ai_msg_instance)

    chat_history.add_message(ai_msg_instance)
    await db.async_session.commit()

    return jsonify(
        {
            "conversation_id": chat_history.id,
            "messages": chat_history.to_dict()["messages"][-20:],
        }
    )
