from tables.table import Table


class User(Table):
    _table_pk = 'id'
    _table_name = 'user'

    def __init__(self, data):
        self.first_name = data[0]
        self.last_name = data[1]
        self.intro = data[2]
        self.birthday = data[3]
        self.id = data[4]
        self.username = data[5]
        self.nationality = data[6]
        self.email = data[7]
        self.address = data[8]
        self.tel_num = data[9]

    @classmethod
    def login(cls, *args, **kwargs):
        res = super().find(kwargs)
        if len(res):
            return {'status': True, 'user': res[0]}
        else:
            return {'status': False}
