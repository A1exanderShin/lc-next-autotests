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
@pytest.mark.xfail(
    reason="BUG: token_refresh returns 500 instead of 4xx on invalid payload",
    strict=True
)
def test_token_refresh_invalid_payload(payload):
    """
    Expected behavior:
    - backend should return 4xx (400/401/403) on invalid payload

    Current behavior:
    - backend returns 500 Internal Server Error
    """
    client = AuthClient()

    resp = client.post("/auth/token_refresh", json=payload)

    assert resp.status_code in (400, 401, 403)


@pytest.mark.xfail(
    reason="BUG: token_refresh returns 500 instead of 4xx on invalid tokens",
    strict=True
)
def test_token_refresh_invalid_tokens():
    """
    Expected behavior:
    - backend should return 4xx on invalid token / refresh_token

    Current behavior:
    - backend returns 500 Internal Server Error
    """
    client = AuthClient()

    resp = client.token_refresh(
        token="invalid-token",
        refresh_token="invalid-refresh-token"
    )

    assert resp.status_code in (400, 401, 403)
