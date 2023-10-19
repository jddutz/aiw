from app import cache
from app.models import ChatSystemMessage

default_instructions = (
    "You are a helpful assistant that helps people with their writing."
)
default_context_message = "Here is some contextual information from the page the user is currently viewing to use at your discretion, as needed."
default_greeting_request = "Starting a new conversation. Greet the user with a welcoming message. Your response should briefly demonstrate an understanding of the context, 'You appear to be working on...', and offer some assistance."


@cache.cached(key_prefix="system_message_instructions")
def get_instructions():
    """Retrieve the instructions message and store it in cache."""

    system_message = ChatSystemMessage.query.filter_by(title="Instructions").first()

    return system_message.content if system_message else default_instructions


@cache.cached(key_prefix="system_message_context")
def get_context_message():
    """Retrieve the context message and store it in cache."""

    system_message = ChatSystemMessage.query.filter_by(title="Context").first()

    return system_message.content if system_message else default_context_message


@cache.cached(key_prefix="system_message_greeting")
def get_greeting_request():
    """Retrieve the greeting message and store it in cache."""

    system_message = ChatSystemMessage.query.filter_by(title="Greeting").first()

    return system_message.content if system_message else default_greeting_request
