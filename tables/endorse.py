from tables.table import Table


class Endorse(Table):
    _table_pk = 'id'
    _table_name = 'Endorse'

    def __init__(self, data):
        self.id = data[0]
        self.skill_id = data[1]
        self.user_id = data[2]
