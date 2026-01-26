from clients.base.base_client import BaseClient


class AuthorizedClient(BaseClient):
    def __init__(self, token: str):
        super().__init__()
        self.session.headers.update({
            "x-access-token": token
        })
