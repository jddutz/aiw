# app/routes/api/v1/chat.py

from flask import request, Blueprint, jsonify


import openai
from app import cache, db
from app.models import ChatHistory, ChatMessage
from app.services import system_messages

chat_api_v1 = Blueprint("chat_api_v1", __name__)


@chat_api_v1.route("/new", methods=["POST"])
def new_conversation():
    chat_history = ChatHistory()
    db.session.add(chat_history)
    db.session.commit()

    # Fetch the cached instructional message or retrieve from DB if not cached
    instructional_message = system_messages.get_instructions()

    messages = [{"role": "system", "content": instructional_message}]

    # Help context id is used to query the system message table for additional context information
    if request.is_json and "help_context_id" in request.json:
        help_context_id = request.json.get("help_context_id")
        if help_context_id:
            help_context_message = system_messages.get_help_context_message()
            help_context = system_messages.get_help_context(help_context_id)
            messages.append(
                {
                    "role": "system",
                    "content": f"{help_context_message}: {help_context}",
                }
            )

    # Retrieve context from the request body
    context_message = system_messages.get_context_message()

    if request.is_json and "page_context" in request.json:
        page_context = request.json.get("page_context")
        messages.append(
            {"role": "system", "content": f"{context_message}: {page_context}"}
        )

    # Append instructions to the AI to greet the user
    messages.append(
        {
            "role": "system",
            "content": system_messages.get_greeting_request(),
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
    chat_history.add_message(ai_msg_instance)

    return jsonify(chat_history.to_dict())


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

    # Compile recent messages for the AI and fetch the system instructional message
    instructional_message = system_messages.get_instructions()

    messages = [{"role": "system", "content": instructional_message}]

    # Help context id is used to query the system message table for additional context information
    if "help_context_id" in request.json:
        help_context_id = request.json.get("help_context_id")
        if help_context_id:
            help_context_message = system_messages.get_help_context_message()
            help_context = system_messages.get_help_context(help_context_id)
            messages.append(
                {
                    "role": "system",
                    "content": f"{help_context_message}: {help_context}",
                }
            )

    # Retrieve context from the request body
    context_message = system_messages.get_context_message()

    if "page_context" in request.json:
        page_context = request.json.get("page_context")
        messages.append(
            {"role": "system", "content": f"{context_message}: {page_context}"}
        )

    # If no conversation_id is provided, create a new ChatHistory
    if chat_history:
        # Extract the last 20 messages and append to messages list
        for msg in chat_history.messages[-20:]:
            messages.append({"role": msg.role, "content": msg.content})
    else:
        chat_history = ChatHistory()
        db.session.add(chat_history)
        db.session.commit()

    # Create and add the user's message to the chat history
    user_msg_instance = ChatMessage(role=ChatMessage.USER, content=user_message)
    chat_history.add_message(user_msg_instance)
    db.session.commit()

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
    chat_history.add_message(ai_msg_instance)
    db.session.commit()

    return jsonify(
        {
            "conversation_id": chat_history.id,
            "messages": chat_history.to_dict()["messages"][-20:],
        }
    )
