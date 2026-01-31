def assert_client_error(resp):
    assert resp.status_code in (400, 401, 403)
