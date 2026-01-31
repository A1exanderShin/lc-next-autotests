from tests.auth.assertions.common_asserts import assert_success


def test_resend_email_happy_path(authorized_user_client):
    resp = authorized_user_client.post("/user/email/resend")
    assert_success(resp)
