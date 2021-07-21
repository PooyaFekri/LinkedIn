from typing import Union

from app import exe_query
from .table import Table


class Message(Table):
    _table_pk = 'id'
    _table_name = 'Message'

    def __init__(self, data):
        self.id = data[0]
        self.user_sender_id = data[1]
        self.user_receiver_id = data[2]
        self.text = data[3]
        self.room_id = data[4]
        self.time = data[5]

    @classmethod
    def insert(cls, *args, **kwargs) -> dict:
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def edit(self, *args, **kwargs):
        try:
            super().update_via_pk(kwargs, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_via_pk(cls, pk: Union[str, int]) -> dict:
        try:
            message = super().find_via_pk(pk)
            return {'status': True, 'message': message}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_messages(cls, room_id):
        query = f'SELECT * FROM {cls._table_name} WHERE room_id = ? ORDER BY time DESC'
        try:
            messages = [Message(message) for message in exe_query(query, room_id)]
            return {'status': True, 'messages': messages}
        except Exception as e:
            return {'status': False, 'error': e}

    @staticmethod
    def get_rooms_info(user_id) -> dict:
        query = f'SELECT DISTINCT room_id, user_receiver_id, user_sender_id from Message where (user_sender_id=? or user_receiver_id=?) group by room_id, user_sender_id, user_receiver_id'
        try:
            rooms_info = [Message(message) for message in exe_query(query, user_id, user_id)]
            return {'status': True, 'rooms_info': rooms_info}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_users_room_id(cls, user1_id, user2_id):
        _filter1 = {
            'user_sender_id': user1_id,
            'user_receiver_id': user2_id
        }

        _filter2 = {
            'user_sender_id': user2_id,
            'user_receiver_id': user1_id
        }
        try:
            messages = super().find(_filter1) + super().find(_filter2)
            room_id = None if not messages else messages[-1].room_id
            return {'status': True, 'room_id': room_id}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find(cls, _filter):
        try:
            messages = super().find(_filter)
            return {'status': True, 'messages': messages}

        except Exception as e:
            return {'status': False, 'error': e}
