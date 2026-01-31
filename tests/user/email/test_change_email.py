import pytest


@pytest.mark.skip(reason="Email confirmation flow is not testable without inbox access")
def test_change_email_happy_path(authorized_user_client):
    pass
