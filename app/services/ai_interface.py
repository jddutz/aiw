# app/services/ai_interface.py

import openai
from sqlalchemy import text
from app import cache, db
from app.models import (
    ChatSystemMessageModel,
    HelpContextModel,
    ChatHistoryModel,
    ChatMessageModel,
    ProjectTemplateModel,
    GenreModel,
)

SYSTEM_GREETING_MESSAGE = "System Greeting Message"


def execute_sql(sql, **kwargs):
    connection = db.engine.connect()
    try:
        result = connection.execute(sql, kwargs).fetchone()

        if result:
            return result[0]
        else:
            return None
    finally:
        connection.close()


def get_system_message(title):
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
                "content": f"{help_context_message}: {help_context.content}",
            }
        )

    if page_content:
        page_content_message = get_system_message("Page Content Message")
        messages.append(
            {"role": "system", "content": f"{page_content_message}: {page_content}"}
        )

    return messages


def start_conversation(
    help_context_id=None,
    page_content=None,
    temperature=0.9,
    openai_model="gpt-3.5-turbo",
):
    chat_history = ChatHistoryModel()
    db.session.add(chat_history)

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
    db.session.commit()

    return chat_history


def send_message(
    chat_history_id,
    message,
    help_context_id=None,
    page_content=None,
    temperature=0.9,
    openai_model="gpt-3.5-turbo",
):
    chat_history = ChatHistoryModel.query.get(chat_history_id)
    messages = init_message_queue(help_context_id, page_content)
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    ai_msg_instance = send(messages, temperature, openai_model)

    chat_history.add_message(ai_msg_instance)
    db.session.commit()

    return chat_history


def send(messages, temperature=0.9, openai_model="gpt-3.5-turbo"):
    # Send the messages to OpenAI
    openai_response = openai.ChatCompletion.create(
        model=openai_model, messages=messages, temperature=temperature
    )

    # Extract the AI's response
    ai_message = openai_response.choices[0].message["content"].strip()

    # Create and add the AI's response to the chat history
    return ChatMessageModel(role=ChatMessageModel.ASSISTANT, content=ai_message)


def get_project_title(description):
    messages = init_message_queue(help_context_id="project.new")
    system_message = get_system_message("New Project Title")
    messages.append({"role": "system", "content": f"{system_message}: {description}"})
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.7
    )
    ai_message = openai_response.choices[0].message["content"].strip()
    return ai_message


def get_project_summary(description):
    messages = init_message_queue(help_context_id="project.new")
    system_message = get_system_message("New Project Summary")
    messages.append({"role": "system", "content": f"{system_message}: {description}"})
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.3
    )
    ai_message = openai_response.choices[0].message["content"].strip()
    return ai_message


def get_project_template(description):
    messages = init_message_queue(help_context_id="project.new")

    project_templates = db.session.query(ProjectTemplateModel.title).all()
    if project_templates:
        templates_str = ", ".join([template.title for template in project_templates])
        messages.append(
            {
                "role": "system",
                "content": f"Available Project Templates: {templates_str}",
            }
        )

    system_message = get_system_message("New Project Template")
    messages.append({"role": "system", "content": f"{system_message}: {description}"})
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.3
    )
    ai_message = openai_response.choices[0].message["content"].strip()

    query = text(
        "SELECT id FROM project_templates WHERE MATCH(title) AGAINST(:search_term) LIMIT 1"
    )
    result = execute_sql(query, search_term=ai_message)

    return result


def get_project_genre(description):
    messages = init_message_queue(help_context_id="project.new")

    genres = db.session.query(GenreModel.name).all()
    if genres:
        genres_str = ", ".join([genre.name for genre in genres])
        messages.append(
            {
                "role": "system",
                "content": f"Available Genres: {genres_str}",
            }
        )

    system_message = get_system_message("New Project Genre")
    messages.append({"role": "system", "content": f"{system_message}: {description}"})

    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.3
    )
    ai_message = openai_response.choices[0].message["content"].strip()

    query = text(
        "SELECT id FROM genres WHERE MATCH(name) AGAINST(:search_term) LIMIT 1"
    )
    result = execute_sql(query, search_term=ai_message)

    return result


def get_project_tags(description):
    messages = init_message_queue(help_context_id="project.new")
    system_message = get_system_message("New Project Tags")
    messages.append({"role": "system", "content": f"{system_message}: {description}"})
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.3
    )
    ai_message = openai_response.choices[0].message["content"].strip()
    return ai_message
