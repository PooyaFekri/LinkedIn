from .table import Table


class Language(Table):
    _table_pk = 'id'
    _table_name = 'Language'

    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.language = data[2]

    @classmethod
    def add(cls, *args, **kwargs):
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
    def find_user_lang(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            languages = super().find(_filter)
            return {'status': True, 'languages': languages}
        except Exception as e:
            return {'status': False, 'error': e}