from .table import Table


class Message(Table):
    _table_pk = 'id'
    _table_name = 'Message'

    def __init__(self, data):
        self.id = data[0]
        self.user_sender_id = data[1]
        self.user_receiver_id = data[2]
        self.text = data[3]
        self.room_id = data[4]
        self.time = data[5]
