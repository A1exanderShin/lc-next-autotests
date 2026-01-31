def assert_payin_redirect(resp):
    data = resp.json()["data"]

    assert "redirect_url" in data
    assert isinstance(data["redirect_url"], str)
    assert data["redirect_url"].startswith("http")


def assert_payin_sms_step(resp):
    data = resp.json()["data"]

    assert data["next_step"] == "SMS_CODE"
