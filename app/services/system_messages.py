from app import cache
from app.models import ChatSystemMessage, HelpContext

default_instructions = (
    "You are a helpful assistant that helps people with their writing."
)
default_context_message = "Here is some contextual information from the page the user is currently viewing to use at your discretion, as needed"
default_help_context_message = "Here is some contextual information about the application to use at your discretion, as needed"
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


@cache.cached(key_prefix="system_message_help_context")
def get_help_context_message():
    """Retrieve the help context message from the database."""

    system_message = ChatSystemMessage.query.filter_by(
        title="Help Context Message"
    ).first()

    return system_message.content if system_message else default_help_context_message


def get_help_context(help_context_id):
    """Retrieve the help context messages from the database."""

    # Retrieve system messages from the database
    help_context = HelpContext.query.filter_by(context_id=help_context_id).first()
    if not help_context:
        return []

    return help_context.content


@cache.cached(key_prefix="system_message_greeting")
def get_greeting_request():
    """Retrieve the greeting message and store it in cache."""

    system_message = ChatSystemMessage.query.filter_by(title="Greeting").first()

    return system_message.content if system_message else default_greeting_request
