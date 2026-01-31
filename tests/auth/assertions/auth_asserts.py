IDENTIFICATION_STATUSES = {
    "accepted",
    "canceled",
    "not_started",
    "pending",
    "waiting",
}


def assert_valid_identification_status(resp):
    data = resp.json()["data"]
    assert data["status"] in IDENTIFICATION_STATUSES

def assert_has_session_id(resp):
    data = resp.json()["data"]
    assert "session_id" in data
    assert isinstance(data["session_id"], str)


def assert_empty_data(resp):
    assert resp.json()["data"] == {}
