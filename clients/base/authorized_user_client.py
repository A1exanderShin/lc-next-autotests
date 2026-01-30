from clients.base.authorized_client import AuthorizedClient
from models.user_context import UserContext


class AuthorizedUserClient(AuthorizedClient):
    def __init__(self, user: UserContext):
        super().__init__(user.token)
        self.user = user
