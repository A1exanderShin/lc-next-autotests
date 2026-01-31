from tests.auth.assertions.common_asserts import assert_success


def test_authorized_access_happy_path(authorized_user_client):
    resp = authorized_user_client.get("/user/me")

    assert_success(resp)