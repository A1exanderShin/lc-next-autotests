import pytest
from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"session_id": "123"},
        {"password": "11111111"},
        {"session_id": "123", "password": ""},
    ],
    ids=[
        "empty_payload",
        "no_password",
        "no_session_id",
        "empty_password",
    ]
)
def test_register_invalid_payload(payload):
    client = AuthClient()

    resp = client.post("/auth/register", json=payload)
    assert resp.status_code in (400, 403)


def test_register_wrong_state():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]

    resp = client.register(session_id, "11111111")

    assert resp.status_code == 403


def test_register_reuse_session_id():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]
    session_id = client.check_sms(session_id, 111111).json()["data"]["session_id"]

    client.register(session_id, "11111111")
    resp = client.register(session_id, "11111111")

    assert resp.status_code >= 400
