from typing import Union

from . import Message
from .table import Table


class Room(Table):
    _table_pk = 'id'
    _table_name = 'Room'

    def __init__(self, data):
        self.id = data[0]
        self.started_time = data[1]
        self.archive = data[2]
        self.user1_id = data[3]
        self.user2_id = data[4]

    @classmethod
    def create(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self, *args, **kwargs):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def archive(self, *args, **kwargs):
        try:
            super().update_via_pk({'archive': True}, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_via_pk(cls, pk: Union[str, int]) -> dict:
        try:
            room = super().find_via_pk(pk)
            return {'status': True, 'room': room}
        except Exception as e:
            return {'status': False, 'error': e}

    def get_messages(self):
        return Message.get_messages(self.id)

    @classmethod
    def room_info(cls, user_id):
        return Message.get_rooms_info(user_id)

    @classmethod
    def find_users_room(cls, user1_id, user2_id):
        _filter1 = {
            'user1_id': user1_id,
            'user2_id': user2_id
        }

        _filter2 = {
            'user1_id': user2_id,
            'user2_id': user1_id
        }
        try:
            rooms = super().find(_filter1) + super().find(_filter2)
            return {'status': True, 'room': rooms[-1]}
        except Exception as e:
            return {'status': False, 'error': e}
