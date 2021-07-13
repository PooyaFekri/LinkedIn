from tables.table import Table


class Comment(Table):
    _table_pk = 'id'
    _table_name = 'Comment'

    def __init__(self, data):
        self.id = data[0]
        self.time = data[1]
        self.user_id = data[2]
        self.text = data[3]
        self.comment_reply_id = data[4]
        self.post_id = data[5]
