def test_authorized_access_happy_path(authorized_user_client):
    resp = authorized_user_client.get("/user/me")

    assert resp.status_code == 200
