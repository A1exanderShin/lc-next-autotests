import os
import psycopg2
import pytest

from db.gambler_repo import GamblerRepo


@pytest.fixture(scope="function")
def gambler_repo():
    password = os.getenv("DB_PASSWORD")

    conn_args = dict(
        host="localhost",
        port="5432",
        dbname="db_game",
        user="postgres",
    )

    # Если пароль есть — добавляем, если нет — не трогаем
    if password:
        conn_args["password"] = password

    connection = psycopg2.connect(**conn_args)

    repo = GamblerRepo(connection)
    yield repo

    connection.close()
