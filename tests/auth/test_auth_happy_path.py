def test_authorized_access_happy_path(authorized_user_client):
    response = authorized_user_client.get("/user/me")  # замени на реальный endpoint

    assert response.status_code == 200, response.text

    body = response.json()
    assert "data" in body
