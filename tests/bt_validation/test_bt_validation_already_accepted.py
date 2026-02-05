import os
import pytest

from clients.bt_validation_client import BtValidationClient
from utils.waiters import wait_until_status_leaves


@pytest.mark.integration
def test_bt_validation_already_accepted_pin(gambler_repo):
    """
    PIN 000003: already accepted; no need validation.

    Contract:
    - FSM must leave waiting_pin
    - FSM may pass through confirming / validation
    - Final accepted depends on async flow (not asserted here)
    """

    phone = "79011550000"
    access_token = os.getenv("TEST_ACCESS_TOKEN")
    assert access_token

    client = BtValidationClient()

    # SETUP
    gambler_repo.set_validation_status(phone, "WAITING")
    client.start(access_token)

    # ACTION
    resp = client.check_sms(access_token, pin="000003")
    assert resp.status_code == 200, resp.text

    # ASSERT
    next_status = wait_until_status_leaves(
        client,
        access_token,
        forbidden_statuses={"waiting_pin"},
        timeout=30,
    )

    # FSM must NOT require waiting_pin for already accepted
    assert next_status in {
        "confirming",
        "validation",
        "accepted",
    }
