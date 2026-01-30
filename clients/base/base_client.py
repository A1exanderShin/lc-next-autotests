import requests
from config.settings import settings


class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "user-agent": "autotests",
            "x-language": "ru",
            "x-app-version": "test"
        })
        self.base_url = settings.base_url
        self.timeout = settings.timeout

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def get(self, path: str, **kwargs):
        return self.session.get(
            self._url(path),
            timeout=self.timeout,
            **kwargs
        )

    def post(self, path: str, **kwargs):
        return self.session.post(
            self._url(path),
            timeout=self.timeout,
            **kwargs
        )

    def put(self, path: str, **kwargs):
        return self.session.put(
            self._url(path),
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, path: str, **kwargs):
        return self.session.delete(
            self._url(path),
            timeout=self.timeout,
            **kwargs
        )
