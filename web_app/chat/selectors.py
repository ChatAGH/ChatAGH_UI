from __future__ import annotations
from typing import Iterable, Union

from django.db.models import QuerySet
from django.contrib.auth.models import User, AnonymousUser
from .models import Conversation, Message


def user_conversations(user: Union[User, AnonymousUser]) -> QuerySet[Conversation]:
    """Return conversations owned by the user."""
    if isinstance(user, AnonymousUser):
        raise ValueError("Anonymous users cannot have conversations.")
    return (
        Conversation.objects.filter(user=user)
        .only("id", "title", "updated_at")
        .order_by("-updated_at")
    )


def conversation_messages(conv: Conversation) -> QuerySet[Message]:
    """Return messages in chronological order for a conversation."""
    return (
        conv.messages.select_related(None)
        .only("id", "role", "content", "created_at")
        .order_by("created_at")
    )


def as_history_tuples(messages: Iterable[Message]) -> list[tuple[str, str]]:
    """
    Convert Message objects to (role, content) tuples for backends that accept history.
    """
    return [(m.role, m.content) for m in messages]


def get_conversations_for_user(user: User) -> QuerySet[Conversation]:
    if isinstance(user, AnonymousUser):
        return Conversation.objects.none()  # Return an empty queryset
    if isinstance(user, User):
        return Conversation.objects.filter(user=user)
    else:
        raise ValueError("Invalid user type")
