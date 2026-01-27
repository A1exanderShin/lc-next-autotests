def login_payload(session_id=None, password=None, accept_offer=True):
    payload = {}

    if session_id is not None:
        payload["session_id"] = session_id

    if password is not None:
        payload["password"] = password

    payload["accept_offer"] = accept_offer
    return payload
