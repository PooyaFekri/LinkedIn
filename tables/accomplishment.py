from .table import Table

class Accomplishment(Table):
    _table_pk = 'id'
    _table_name = 'Accomplishment'

    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.title = data[2]
        self.accomplishment_time = data[3]
        self.time = data[4]

    @classmethod
    def create(cls, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_accomplishments_by_user_id(cls, user_id):
        _filter = {
            'user_id': user_id,
        }
        try:
            accomplishments = super().find(_filter)
            return {'status': True, 'accomplishments': accomplishments}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def update(self, **kwargs):
        try:
            super().update_via_pk(kwargs, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

