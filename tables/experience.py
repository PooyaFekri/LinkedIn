from tables.table import Table


class Experience(Table):
    _table_pk = 'id'
    _table_name = 'Experience'

    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.text = data[2]
