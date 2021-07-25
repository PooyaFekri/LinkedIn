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
    def create(cls):
        pass

    @classmethod
    def get_accomplishments_by_user_id(cls):
        pass

    def delete(self):
        pass

    def update(self):
        pass

