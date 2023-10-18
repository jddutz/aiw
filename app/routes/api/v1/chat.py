# app/routes/api/v1/chat.py

from flask import request, Blueprint, jsonify


import openai
from datetime import datetime
from app import db
from app.models import ChatHistory, ChatMessage, ChatSystemMessage

chat_api_v1 = Blueprint("chat_api_v1", __name__)


@chat_api_v1.route("/new", methods=["GET"])
def new_conversation():
    chat_history = ChatHistory()
    db.session.add(chat_history)
    db.session.commit()
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
    instructional_message = (
        ChatSystemMessage.query.filter_by(title="AI Instructional Message")
        .first()
        .content
    )
    messages = [{"role": "system", "content": instructional_message}]

    # If no conversation_id is provided, create a new ChatHistory
    if chat_history:
        # Extract the last 5 user messages and append to messages list
        for msg in chat_history.messages[-5:]:
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

    return jsonify(ai_msg_instance.to_dict())
