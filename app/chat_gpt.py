# app/chat_gpt.py

import db.conversations
import db.projects
import os
import openai
from typing import List, Union, Dict
from models import WritingProjectModel, ChatHistoryModel, ChatMessageModel
import uuid

openai.api_key = os.environ["OPENAI_API_KEY"]

system_message = {
    "role": "system",
    "content": "You are an AI assistant that helps amateur writers with creative writing projects.",
}


def chat(
    input: str, conversation_id: str = None, project_id: str = None
) -> Union[str, None]:
    # Prepend the system message
    messages = [system_message]

    # Prepend the project info
    if project_id is None:
        project_id = str(uuid.uuid4())
        messages.append(
            {
                "role": "system",
                "content": "The current project is undefined. Summarize the idea provided and suggest some working titles, or provide some guidance on how to get started and a few random writing prompts related to the user's message.",
            }
        )
    else:
        project = db.projects.get(project_id)
        messages.append(
            {
                "role": "system",
                "content": f"Project Title: {project.title}\nDescription: {project.description}",
            }
        )

    # Retrieve the history for the given ID or initialize a new one
    chat_history = db.conversations.get_or_create(conversation_id)

    # Append user's message to the history
    chat_message = ChatMessageModel(role="user", content=input)

    chat_history.messages.append(chat_message)

    messages.append({"role": "user", "content": chat_message.content})

    try:
        chatgpt_response = openai.ChatCompletion.create(
            model="gpt-4", messages=messages  # GPT-4 model
        )
        response = chatgpt_response.choices[0].message["content"].strip()

    except Exception as e:
        return f"Error while communicating with ChatGPT: {e}"

    # Store the AI's response in history
    chat_history.messages.append(ChatMessageModel(role="assistant", content=response))

    db.conversations.save(chat_history)

    return response
