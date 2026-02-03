def assert_payout_redirect(resp):
    data = resp.json()["data"]

    assert "redirect_url" in data
    assert isinstance(data["redirect_url"], str)
    assert data["redirect_url"].startswith("http")

def assert_payout_info(resp):
    body = resp.json()

    assert body["code"] == 200

    data = body["data"]
    assert isinstance(data, dict)

    assert "tax" in data
    assert isinstance(data["tax"], dict)

    assert "min" in data["tax"]
    assert isinstance(data["tax"]["min"], int)

    assert "ratio" in data["tax"]
    assert isinstance(data["tax"]["ratio"], (int, float))

    assert "retention" in data
    assert "delay" in data

def assert_payout_created(resp):
    body = resp.json()

    assert body["code"] == 200
    data = body.get("data", {})

    # контракт минимальный и стабильный
    assert isinstance(data, dict)
