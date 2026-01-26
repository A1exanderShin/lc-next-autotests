import pytest
from clients.base.authorized_user_client import AuthorizedUserClient


@pytest.fixture(scope="session")
def authorized_user_client(user_context):
    return AuthorizedUserClient(user_context)
