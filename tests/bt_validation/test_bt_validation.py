import os
import pytest

from clients.bt_validation_client import BtValidationClient


@pytest.mark.integration
def test_bt_validation_happy_path(gambler_repo):
    phone = "79011550000"

    access_token = os.getenv("TEST_ACCESS_TOKEN")
    assert access_token, "TEST_ACCESS_TOKEN env variable is required"

    client = BtValidationClient()

    # 1. Приводим пользователя в нужное состояние
    gambler_repo.set_validation_status(phone, "WAITING")

    # 2. Start validation
    resp = client.start(access_token=access_token)
    assert resp.status_code == 200, resp.text

    # 3. Check SMS
    resp = client.check_sms(access_token=access_token)
    assert resp.status_code == 200, resp.text

    data = resp.json()["data"]

    # Процесс успешно принят внешним сервисом
    assert data["status"] not in ("error", "failed")
    assert data["finished"] is None
    assert data["error_code"] is None
