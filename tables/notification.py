from app import exe_query
from .table import Table


class Notification(Table):
    _table_pk = 'id'
    _table_name = 'Notification'

    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.type_id = data[2]
        self.type = data[3]
        self.time = data[4]
        self.event = data[5]
        self.visited = data[6]

    @classmethod
    def notify(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def visit_notification(self):
        data = {'visited': True}
        try:
            super().update_via_pk(data, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def user_notification(cls, user_id):
        query = f'SELECT * from {cls._table_name} WHERE user_id=? and visited=? ORDER BY time DESC'
        try:
            notifications = exe_query(query, user_id, False)
            return {'status': True, 'notifications': notifications}
        except Exception as e:
            return {'status': False, 'error': e}
