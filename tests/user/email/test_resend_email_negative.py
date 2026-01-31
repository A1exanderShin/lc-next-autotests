from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


def test_resend_email_unauthorized():
    client = AuthClient()

    resp = client.post("/user/email/resend")

    assert_client_error(resp)
