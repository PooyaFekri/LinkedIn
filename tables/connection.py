from typing import Union

from app import exe_query
from .table import Table


class Connection(Table):
    _table_pk = 'id'
    _table_name = 'Connection'

    def __init__(self, data):
        self.id = data[0]
        self.user_caller_id = data[1]
        self.user_invited_id = data[2]
        self.connected = data[3]

    @classmethod
    def connect_request(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def accept_request(self, user_caller_id):
        try:
            super().update_via_pk({'user_caller_id': user_caller_id}, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_via_pk(cls, pk: Union[str, int]) -> 'dict':
        try:
            connection = super().find_via_pk(pk)
            return {'status': True, 'connection': connection}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_user_connections(cls, user_id):
        _filter = {
            'user_invited_id': user_id,
            'user_caller_id': user_id
        }
        query = f'SELECT * from {cls._table_name} WHERE user_caller_id=? or user_invited_id=?'
        try:
            connections = exe_query(query, user_id, user_id)
            return {'status': True, 'connections': connections}
        except Exception as e:
            return {'status': False, 'error': e}