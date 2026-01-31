def assert_valid_user_me(resp_json: dict):
    data = resp_json["data"]

    assert isinstance(data["gambler_id"], int)
    assert isinstance(data["phone"], str)

    assert "reg_dttm" in data
    assert isinstance(data["approved_email"], bool)

    # nullable поля
    assert "email" in data
    assert "avatar_url" in data
