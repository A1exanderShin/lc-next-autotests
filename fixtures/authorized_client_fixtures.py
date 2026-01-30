import pytest
from clients.base.authorized_user_client import AuthorizedUserClient
from fixtures.user_context_fixture import user_context


@pytest.fixture(scope="session")
def authorized_user_client(user_context):
    return AuthorizedUserClient(user_context)
