import os
import pytest

from clients.bt_validation_client import BtValidationClient
from utils.waiters import (
    wait_until_status_equals,
    wait_until_status_leaves,
)


@pytest.mark.integration
def test_bt_validation_happy_path(gambler_repo):
    """
    Happy-path until async phase.
    We do NOT wait for accepted (external service).
    """

    phone = "79011550000"
    access_token = os.getenv("TEST_ACCESS_TOKEN")
    assert access_token

    client = BtValidationClient()

    # SETUP
    gambler_repo.set_validation_status(phone, "WAITING")

    # START
    resp = client.start(access_token)
    assert resp.status_code == 200

    wait_until_status_equals(
        client, access_token, expected_status="waiting_pin"
    )

    # CHECK SMS (valid pin)
    resp = client.check_sms(access_token, pin="000000")
    assert resp.status_code == 200

    # ASSERT: FSM left waiting_pin
    next_status = wait_until_status_leaves(
        client,
        access_token,
        forbidden_statuses={"waiting_pin"},
    )

    assert next_status != "waiting_pin"
