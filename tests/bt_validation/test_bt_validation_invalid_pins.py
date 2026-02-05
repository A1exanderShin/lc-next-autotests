import os
import pytest

from clients.bt_validation_client import BtValidationClient
from utils.waiters import wait_until_status_leaves


INVALID_PINS = [
    "000001",  # confirmBtSession error; on reply
    "000002",  # confirmBtSession error; async
    "000006",  # incorrect pin
    "000007",  # attempts exceeded
]


@pytest.mark.integration
@pytest.mark.parametrize("pin", INVALID_PINS)
def test_bt_validation_invalid_pins_do_not_accept(gambler_repo, pin):
    """
    Invalid PIN must NOT result in accepted status.
    FSM may still move forward asynchronously.
    """

    phone = "79011550000"
    access_token = os.getenv("TEST_ACCESS_TOKEN")
    assert access_token

    client = BtValidationClient()

    # SETUP
    gambler_repo.set_validation_status(phone, "WAITING")
    client.start(access_token)

    # ACTION
    resp = client.check_sms(access_token, pin=pin)
    assert resp.status_code == 200, resp.text

    # ASSERT
    next_status = wait_until_status_leaves(
        client,
        access_token,
        forbidden_statuses={"waiting_pin"},
        timeout=30,
    )

    assert next_status != "accepted"
