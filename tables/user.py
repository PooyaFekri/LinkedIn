import datetime
from typing import Union

from app import exe_query
from . import Connection
from .notification import Notification
from .table import Table


class User(Table):
    _table_pk = 'id'
    _table_name = 'user'

    def __init__(self, data):
        self.first_name = data[0]
        self.last_name = data[1]
        self.intro = data[2]
        self.birthday = data[3]
        self.id = data[4]
        self.username = data[5]
        self.nationality = data[6]
        self.email = data[7]
        self.address = data[8]
        self.tel_num = data[9]

    @classmethod
    def login(cls, *args, **kwargs):
        res = super().find(kwargs)
        if len(res):
            '''
            {status : (false or true), user: user object}
            '''
            return {'status': True, 'user': res[0]}
        else:
            return {'status': False, 'error': 'invalid username or password'}

    @classmethod
    def signup(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            '''
                { status : (false or true), error : cause of error}
            '''
            return {'status': False, 'error': e}

    def delete(self, *args, **kwargs):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def update(self, *args, **kwargs):
        try:
            super().update_via_pk(kwargs, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_users(cls, *args, **kwargs):
        try:
            users = super().find(kwargs)
            return {'status': True, 'users': users}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_via_pk(cls, pk: Union[str, int]) -> dict:
        try:
            user = super().find_via_pk(pk)
            return {'status': True, 'user': user}
        except Exception as e:
            return {'status': False, 'error': e}

    def people_user_may_know(self):
        try:
            connections = Connection.find_user_connections(self.id).get('connections')
            users = []
            for connection in connections:
                connect_user_id = connection.user_caller_id if connection.user_caller_id != self.id else connection.user_invited_id
                user2_connections = Connection.find_user_connections(connect_user_id).get('connections')

                for user2_connection in user2_connections:
                    connect_user2_id = user2_connection.user_caller_id if user2_connection.user_caller_id != connect_user_id else user2_connection.user_invited_id
                    if self.id != connect_user2_id and not Connection.get_connect_with_users_id(self.id, connect_user2_id).get('connection'):
                        user = self.find_via_pk(connect_user2_id).get('user')
                        users.append(user)
            return {'status': True, 'users': users}
        except Exception as e:
            return {'status': False, 'error': e}

    def search(self, username):
        query = f'SELECT * FROM user WHERE username LIKE ? and id != ?'
        username = f'%{username}%'
        try:
            res_users = [User(user) for user in exe_query(query, username, self.id)]
            users = []
            for user in res_users:
                if Connection.get_connect_with_users_id(self.id, user.id).get('connection'):
                    continue
                users.append(user)

            return {'status': True, 'users': users}
        except Exception as e:
            return {'status': False, 'error': e}

    def birthday_notification(self):
        try:
            notifications = Notification.user_notification(self.id).get('notifications')
            connections = Connection.find_user_connections(self.id).get('connections')
            for connection in connections:
                connect_user_id = connection.user_caller_id if connection.user_caller_id != self.id \
                    else connection.user_invited_id
                user = User.find_via_pk(connect_user_id).get('user')
                date = user.birthday.split()[0]
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                now = datetime.datetime.now()
                if date.month == now.month and date.day == now.day:
                    for notification in notifications:
                        notification_time = notification.time.split()[0]
                        notification_time = datetime.datetime.strptime(notification_time, '%Y-%m-%d')
                        if notification.type == 'user' and notification.type_id == connect_user_id \
                                and notification_time.year == now.year and notification.event == 'birthday':
                            break
                    else:
                        data = {
                            'type': 'user',
                            'type_id': connect_user_id,
                            'event': 'birthday',
                            'user_id': self.id,
                            'time': now
                        }
                        Notification.notify(**data)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}