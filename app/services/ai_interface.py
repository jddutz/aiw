# app/services/ai_interface.py

import openai
from app import cache, db
from app.models import (
    ChatSystemMessageModel,
    HelpContextModel,
    ChatHistoryModel,
    ChatMessageModel,
)

SYSTEM_GREETING_MESSAGE = "System Greeting Message"


async def get_system_message(title):
    message = ChatSystemMessageModel.query.filter_by(title=title).first()

    if not message:
        raise ValueError(f"Could not find a system message with the title {title}")

    return message.content


def init_message_queue(help_context_id=None, page_content=None):
    messages = []

    initialization_message = get_system_message("Initialization")
    messages.append({"role": "system", "content": initialization_message})

    if help_context_id:
        help_context = HelpContextModel.query.filter_by(
            context_id=help_context_id
        ).first()

        if not help_context:
            raise ValueError(f"Could not find help context, {help_context_id}")

        help_context_message = get_system_message("Help Context Message")
        messages.append(
            {
                "role": "system",
                "content": f"{help_context_message.content}: {help_context.content}",
            }
        )

    if page_content:
        page_content_message = get_system_message("Page Content Message")
        messages.append(
            {"role": "system", "content": f"{page_content_message}: {page_content}"}
        )

    return messages


async def start_conversation(
    help_context_id=None,
    page_content=None,
    temperature=0.9,
    openai_model="gpt-3.5-turbo",
):
    chat_history = ChatHistoryModel()
    await db.async_session.add(chat_history)

    messages = init_message_queue(help_context_id, page_content)

    greeting = ChatSystemMessageModel.query.filter_by(
        title=SYSTEM_GREETING_MESSAGE
    ).first()

    # Append instructions to the AI to greet the user
    messages.append(
        {
            "role": "system",
            "content": greeting.content,
        }
    )

    ai_msg_instance = send(messages, temperature, openai_model)

    chat_history.add_message(ai_msg_instance)
    await db.async_session.commit()

    return chat_history


async def send_message(
    chat_history_id,
    message,
    help_context_id=None,
    page_content=None,
    temperature=0.9,
    openai_model="gpt-3.5-turbo",
):
    chat_history = await ChatHistoryModel.query.get(chat_history_id)
    messages = init_message_queue(help_context_id, page_content)
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    ai_msg_instance = send(messages, temperature, openai_model)

    chat_history.add_message(ai_msg_instance)
    await db.async_session.commit()

    return chat_history


async def send(messages, temperature=0.9, openai_model="gpt-3.5-turbo"):
    # Send the messages to OpenAI
    openai_response = await openai.ChatCompletion.create(
        model=openai_model, messages=messages, temperature=temperature
    )

    # Extract the AI's response
    ai_message = openai_response.choices[0].message["content"].strip()

    # Create and add the AI's response to the chat history
    return ChatMessageModel(role=ChatMessageModel.ASSISTANT, content=ai_message)


async def get_project_title(description):
    messages = [
        {
            "role": "system",
            "content": "Project Title",
        },
        {
            "role": "user",
            "content": description,
        },
    ]
    openai_response = await openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.1
    )


async def get_project_summary(description):
    pass


async def get_project_template(description):
    pass


async def get_project_genre(description):
    pass


async def get_project_tags(description):
    pass
