# app/routes/api/v1/chat.py

from flask import request, Blueprint, jsonify


import openai
from app import cache, db
from app.models import ChatSystemMessage, HelpContext, ChatHistory, ChatMessage

chat_api_v1 = Blueprint("chat_api_v1", __name__)

INITIALIZATION_MESSAGE_TITLE = "Initialization"
HELP_CONTEXT_MESSAGE_TITLE = "Help Context Message"
PAGE_CONTEXT_MESSAGE_TITLE = "Page Context Message"
SYSTEM_GREETING_MESSAGE_TITLE = "System Greeting Message"


def init_message_queue():
    # Fetch the cached instructional message or retrieve from DB if not cached
    initialization_message = ChatSystemMessage.query.filter_by(
        title=INITIALIZATION_MESSAGE_TITLE
    ).first()

    messages = [{"role": "system", "content": initialization_message.content}]

    # Help context id is used to query the system message table for additional context information
    if request.is_json and "help_context_id" in request.json:
        help_context_id = request.json.get("help_context_id")

    if help_context_id:
        help_context_message = ChatSystemMessage.query.filter_by(
            title=HELP_CONTEXT_MESSAGE_TITLE
        ).first()

    if help_context_message:
        help_context = HelpContext.query.filter_by(context_id=help_context_id).first()

    if help_context:
        messages.append(
            {
                "role": "system",
                "content": f"{help_context_message.content}: {help_context.content}",
            }
        )

    if request.is_json and "page_context" in request.json:
        # Retrieve context from the request body
        page_context_message = ChatSystemMessage.query.filter_by(
            title=PAGE_CONTEXT_MESSAGE_TITLE
        ).first()

    if page_context_message:
        page_context = request.json.get("page_context")

    if page_context:
        messages.append(
            {
                "role": "system",
                "content": f"{page_context_message.content}: {page_context}",
            }
        )

    return messages


@chat_api_v1.route("/new", methods=["POST"])
def new_conversation():
    chat_history = ChatHistory()
    db.session.add(chat_history)

    messages = init_message_queue()

    greeting = ChatSystemMessage.query.filter_by(
        title=SYSTEM_GREETING_MESSAGE_TITLE
    ).first()

    # Append instructions to the AI to greet the user
    messages.append(
        {
            "role": "system",
            "content": greeting.content,
        }
    )

    # Check the current temperature
    if "temperature" in request.json:
        temperature = request.json["temperature"]
    else:
        temperature = 0.9

    # Send the messages to OpenAI
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=temperature
    )

    ai_message = openai_response.choices[0].message["content"].strip()

    # Create and add the AI's response to the chat history
    ai_msg_instance = ChatMessage(role=ChatMessage.ASSISTANT, content=ai_message)
    db.session.add(ai_msg_instance)

    chat_history.add_message(ai_msg_instance)
    db.session.commit()

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


@chat_api_v1.route("/<int:conversation_id>", methods=["GET"])
def get_conversation(conversation_id):
    chat_history = ChatHistory.query.get(conversation_id)
    if chat_history is None:
        return jsonify({"error": "Conversation not found"}), 404
    return jsonify(chat_history.to_dict())


@chat_api_v1.route("/", methods=["POST"])
@chat_api_v1.route("/<int:conversation_id>", methods=["POST"])
def send_message(conversation_id=None):
    if not request.is_json:
        return jsonify({"error": "Request mimetype must be application/json"}), 400

    if not "content" in request.json:
        return jsonify({"error": "Message content is required"}), 400

    user_message = request.json.get("content")

    chat_history = None
    if conversation_id:
        chat_history = ChatHistory.query.get(conversation_id)
        if chat_history is None:
            return jsonify({"error": "Conversation not found"}), 404

    messages = init_message_queue()

    # If no conversation_id is provided, create a new ChatHistory
    if chat_history:
        # Extract the last 20 messages and append to messages list
        for msg in chat_history.messages[-20:]:
            messages.append({"role": msg.role, "content": msg.content})
    else:
        chat_history = ChatHistory()
        db.session.add(chat_history)

    # Create and add the user's message to the chat history
    user_msg_instance = ChatMessage(role=ChatMessage.USER, content=user_message)
    db.session.add(user_msg_instance)

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
    ai_msg_instance = ChatMessage(role=ChatMessage.ASSISTANT, content=ai_message)
    db.session.add(ai_msg_instance)

    chat_history.add_message(ai_msg_instance)
    db.session.commit()

    return jsonify(
        {
            "conversation_id": chat_history.id,
            "messages": chat_history.to_dict()["messages"][-20:],
        }
    )
