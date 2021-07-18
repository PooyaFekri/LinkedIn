from .table import Table


class Endorse(Table):
    _table_pk = 'id'
    _table_name = 'Endorse'

    def __init__(self, data):
        self.id = data[0]
        self.skill_id = data[1]
        self.user_id = data[2]

    @classmethod
    def create(cls, *args, **kwargs):
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

    @classmethod
    def find_user_endorses(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            endorse = super().find(_filter)
            return {'status': True, 'endorse': endorse}
        except Exception as e:
            return {'status': False, 'error': e}
