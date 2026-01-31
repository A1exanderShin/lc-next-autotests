from tests.auth.assertions.common_asserts import assert_success


def test_get_user_wallet_happy_path(authorized_user_client):
    resp = authorized_user_client.get("/user/wallet")

    assert_success(resp)

    data = resp.json()["data"]
    wallet = data["wallet"]

    assert wallet["balance"] >= 0
    assert wallet["bonus_balance"] >= 0

    assert data["loyalty_status"] is None or data["loyalty_status"] in {
        "Standart",
        "Silver",
        "Gold",
        "Premium",
    }
