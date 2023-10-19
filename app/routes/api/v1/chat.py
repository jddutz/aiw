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

    # Retrieve context from the request body
    context_message = system_messages.get_context_message()

    if request.is_json and "context" in request.json:
        context = request.json.get("context")
        context_text = f"{context_message}: {context}"
        messages.append({"role": "system", "content": context_text})

    # Append instructions to the AI to greet the user
    messages.append(
        {
            "role": "system",
            "content": system_messages.get_greeting_request(),
        }
    )

    # Send the messages to OpenAI
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
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
    chat_history = None
    if conversation_id:
        chat_history = ChatHistory.query.get(conversation_id)
        if chat_history is None:
            return jsonify({"error": "Conversation not found"}), 404

    user_message = request.json.get("content")
    if not user_message:
        return jsonify({"error": "Message content required"}), 400

    # Compile recent messages for the AI and fetch the system instructional message
    instructional_message = system_messages.get_instructions()

    messages = [{"role": "system", "content": instructional_message}]

    # Retrieve context from the request body
    context_message = system_messages.get_context_message()

    if request.is_json and "context" in request.json:
        context = request.json.get("context")
        context_text = f"{context_message}: {context}"
        messages.append({"role": "system", "content": context_text})

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

    # Send the messages to OpenAI
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

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
