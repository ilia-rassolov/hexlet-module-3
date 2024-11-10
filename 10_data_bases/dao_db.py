import psycopg2
from psycopg2.extras import DictCursor
from dao_models import User


def get_connection():
    return psycopg2.connect(
        dbname='hexlet', user='user',
        cursor_factory=DictCursor
    )


def commit(conn):
    conn.commit()


def save_user(conn, user):
    with conn.cursor() as cur:
        if user.id is None:
            cur.execute(
                "INSERT INTO users (username, phone) VALUES (%s, %s) RETURNING id;",
                (user.username, user.phone)
            )
            user.id = cur.fetchone()['id']
        else:
            cur.execute(
                "UPDATE users SET username = %s, phone = %s WHERE id = %s;",
                (user.username, user.phone, user.id)
            )
    return user


def find_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        result = cur.fetchone()
        if result:
            return User(**result)
    return None


def drop_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM users WHERE id = %s;",
            (user_id,))
