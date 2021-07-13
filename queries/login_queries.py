import sqlite3
from sqlite3 import Error
from tables.user import User


def create_connection(db_file, *args, **kwargs):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        login(conn, args, **kwargs)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def login(*args, **kwargs):
    rows = User.login(**kwargs)
    for row in rows:
        print(row)


if __name__ == '__main__':
    login(username='pooyaa', password='1234')
