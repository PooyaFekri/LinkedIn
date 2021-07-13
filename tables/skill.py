from tables.table import Table


class Skill(Table):
    _table_pk = 'id'
    _table_name = 'skill'

    def __init__(self, data):
        self.user_id = data[0]
        self.id = data[1]
        self.text = data[2]
