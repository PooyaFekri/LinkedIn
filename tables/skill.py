from .table import Table


class Skill(Table):
    _table_pk = 'id'
    _table_name = 'skill'

    def __init__(self, data):
        self.user_id = data[0]
        self.id = data[1]
        self.text = data[2]

    @classmethod
    def insert(cls, *args, **kwargs) -> dict:
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def update(self, *args, **kwargs):
        try:
            super().update_via_pk(kwargs, self.id)
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
    def find_user_id(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            skills = super().find(_filter)
            return {'status': True, 'skills': skills}
        except Exception as e:
            return {'status': False, 'error': e}
