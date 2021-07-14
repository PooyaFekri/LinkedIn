from .table import Table


class Like(Table):
    _table_pk = 'id'
    _table_name = 'Like'

    def __init__(self, data):
        self.id = data[0]
        self.comment_id = data[1]
        self.post_id = data[2]
        self.time = data[3]
