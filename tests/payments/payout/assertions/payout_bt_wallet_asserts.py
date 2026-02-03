def assert_payout_bt_wallet_redirect(resp):
    data = resp.json()["data"]

    assert "redirect_url" in data
    assert isinstance(data["redirect_url"], str)
    assert data["redirect_url"].startswith("http")

