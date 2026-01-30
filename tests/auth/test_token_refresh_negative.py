import pytest
from clients.auth_client import AuthClient


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"token": "some-token"},
        {"refresh_token": "some-refresh"},
    ],
    ids=[
        "empty_payload",
        "no_refresh_token",
        "no_token",
    ]
)
def test_token_refresh_invalid_payload(payload):
    client = AuthClient()

    resp = client.post("/auth/token_refresh", json=payload)
    assert resp.status_code >= 400


def test_token_refresh_invalid_tokens():
    client = AuthClient()

    resp = client.token_refresh(
        token="invalid-token",
        refresh_token="invalid-refresh-token"
    )

    assert resp.status_code >= 400
