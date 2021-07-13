import datetime
import sqlite3
from sqlite3 import Error
from tables import User


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


def login(*args, **kwargs) -> 'User':
    res = User.login(**kwargs)
    return res.get('user')


def signup(*args, **kwargs):
    print(User.signup(**kwargs))


if __name__ == '__main__':
    # signup(first_name='pooya', last_name='fekri', username='pooya', password='1234',
    #        birthday=datetime.datetime.strptime('2021-07-13', '%Y-%m-%d'), nationality='iran', email='pooya@gmail.com')
    user = login(username='pooya', password='1234')
    # user.delete()
    user.update(first_name='pooyaaa', last_name='fekri', username='pooya', password='1234',
                birthday=datetime.datetime.strptime('2021-07-13', '%Y-%m-%d'), nationality='iran',
                email='pooya@gmail.com')
