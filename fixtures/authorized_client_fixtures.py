import pytest
from clients.base.authorized_user_client import AuthorizedUserClient
from models.user_context import UserContext


@pytest.fixture(scope="session")
def authorized_user_client(user_context):
    """
    Session user — auth, read-only, base user tests
    """
    return AuthorizedUserClient(user_context)


@pytest.fixture
def authorized_fresh_user_client(fresh_user):
    """
    Fresh user — stateful tests (password, payments)
    """
    user_context = UserContext(
        token=fresh_user["token"],
        session_id=None,  # не нужен для user/password
    )
    return AuthorizedUserClient(user_context)
