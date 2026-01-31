from tests.auth.assertions.auth_asserts import assert_valid_identification_status
from tests.auth.assertions.common_asserts import assert_success


def test_identification_status_happy_path(authorized_user_client):
    resp = authorized_user_client.get("/identification/status")

    assert_success(resp)
    assert_valid_identification_status(resp)
