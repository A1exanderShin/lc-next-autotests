import time


def wait_until_status_equals(
    client,
    access_token: str,
    expected_status: str,
    timeout: int = 30,
    poll_interval: float = 1.0,
):
    start = time.time()
    last_status = None

    while time.time() - start < timeout:
        resp = client.status(access_token)
        assert resp.status_code == 200, resp.text

        last_status = resp.json()["data"]["status"]

        if last_status == expected_status:
            return last_status

        time.sleep(poll_interval)

    raise AssertionError(
        f"Timeout waiting for status='{expected_status}', "
        f"last_status='{last_status}'"
    )


def wait_until_status_leaves(
    client,
    access_token: str,
    forbidden_statuses: set[str],
    timeout: int = 30,
    poll_interval: float = 1.0,
):
    start = time.time()
    last_status = None

    while time.time() - start < timeout:
        resp = client.status(access_token)
        assert resp.status_code == 200, resp.text

        last_status = resp.json()["data"]["status"]

        if last_status not in forbidden_statuses:
            return last_status

        time.sleep(poll_interval)

    raise AssertionError(
        f"Timeout waiting for status to leave {forbidden_statuses}, "
        f"last_status='{last_status}'"
    )
