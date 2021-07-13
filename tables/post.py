from tables.table import Table


class Post(Table):
    _table_pk = 'id'
    _table_name = 'Post'

    def __init__(self, data):
        self.user_id = data[0]
        self.id = data[1]
        self.picture = data[2]
        self.text = data[3]
        self.time = data[4]
        self.share = data[5]
