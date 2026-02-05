import os
import pytest

from clients.bt_validation_client import BtValidationClient
from utils.waiters import wait_until_status_leaves


@pytest.mark.integration
@pytest.mark.parametrize(
    "pin",
    [
        "000004",  # timeout → accepted
        "000005",  # canceled
    ],
)
def test_bt_validation_async_negative_results(gambler_repo, pin):
    phone = "79011550000"
    access_token = os.getenv("TEST_ACCESS_TOKEN")
    assert access_token

    client = BtValidationClient()

    gambler_repo.set_validation_status(phone, "WAITING")
    client.start(access_token)

    resp = client.check_sms(access_token, pin=pin)
    assert resp.status_code == 200

    next_status = wait_until_status_leaves(
        client,
        access_token,
        forbidden_statuses={"waiting_pin"},
        timeout=60,
    )

    # FSM must complete async phase
    assert next_status in {
        "accepted",
        "canceled",
        "validation",
        "confirming",
    }
