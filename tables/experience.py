from .table import Table


class Experience(Table):
    _table_pk = 'id'
    _table_name = 'Experience'

    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.text = data[2]
        self.start_time = data[3]
        self.end_time = data[4]

    @classmethod
    def add(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
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
    def find_user_experiences(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            experiences = super().find(_filter)
            return {'status': True, 'experiences': experiences}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

