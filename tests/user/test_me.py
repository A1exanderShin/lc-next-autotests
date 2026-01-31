from tests.user.assertions.user_asserts import assert_valid_user_me
from tests.auth.assertions.common_asserts import assert_success


def test_get_user_me_happy_path(authorized_user_client):
    resp = authorized_user_client.get("/user/me")

    assert_success(resp)
    assert_valid_user_me(resp.json())
