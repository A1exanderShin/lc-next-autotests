import time


class GamblerRepo:
    def __init__(self, connection):
        self.connection = connection

    def set_validation_status(self, phone: str, status: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE game.gamblers
                SET validation_status = %s
                WHERE phone = %s
                """,
                (status, phone),
            )
        self.connection.commit()

    def has_any_with_status(self, phone: str, status: str) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM game.gamblers
                WHERE phone = %s
                  AND validation_status = %s
                """,
                (phone, status),
            )
            return cursor.fetchone()[0] > 0

    def wait_for_any_validation_status(
        self,
        phone: str,
        expected_status: str,
        timeout: int = 30,
        poll_interval: float = 1.0,
    ):
        start = time.time()

        while time.time() - start < timeout:
            if self.has_any_with_status(phone, expected_status):
                return

            time.sleep(poll_interval)

        raise AssertionError(
            f"Timeout waiting for ANY gambler with status={expected_status}, phone={phone}"
        )
