from tables.table import Table


class Room(Table):
    _table_pk = 'id'
    _table_name = 'Room'

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.started_time = data[2]
        self.archive = data[3]
