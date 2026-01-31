def assert_client_error(resp):
    assert resp.status_code in (400, 403)


def assert_success(resp):
    assert resp.status_code == 200
