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
        _filter = {
            'room_id': room_id
        }
        try:
            messages = super().find(_filter)
            return {'status': True, 'messages': messages}
        except Exception as e:
            return {'status': False, 'error': e}

    @staticmethod
    def get_rooms_info(user_id: str) -> dict:
        query = f'SELECT DISTINCT room_id, user_receiver_id, user_sender_id from Message where user_sender_id=? or user_receiver_id=? group by room_id, user_sender_id, user_receiver_id'
        try:
            rooms_info = exe_query(query, user_id, user_id)
            return {'status': True, 'rooms_id': rooms_info}
        except Exception as e:
            return {'status': False, 'error': e}

