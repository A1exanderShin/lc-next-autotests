from clients.auth_client import AuthClient
from tests.auth.helpers import login_payload


def test_login_invalid_password(user_context):
    client = AuthClient()

    payload = login_payload(
        session_id=user_context.session_id,
        password="wrong_password"
    )

    response = client.login(**payload)

    assert 400 <= response.status_code < 500


def test_login_empty_password(user_context):
    client = AuthClient()

    payload = login_payload(
        session_id=user_context.session_id,
        password=""
    )

    response = client.login(**payload)

    assert 400 <= response.status_code < 500


def test_login_invalid_session_id():
    client = AuthClient()

    payload = login_payload(
        session_id="invalid-session-id",
        password="00000000"
    )

    response = client.login(**payload)

    assert 400 <= response.status_code < 500


def test_login_without_session_id():
    client = AuthClient()

    response = client.login(
        session_id=None,
        password="00000000"
    )

    assert 400 <= response.status_code < 500
