from .table import Table


class Like(Table):
    _table_pk = 'id'
    _table_name = 'Like'

    def __init__(self, data):
        self.id = data[0]
        self.comment_id = data[1]
        self.post_id = data[2]
        self.time = data[3]

    @classmethod
    def like(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_post_likes(cls, post_id):
        _filter = {
            'post_id': post_id
        }
        try:
            likes = super().find(_filter)
            return {'status': True, 'likes': likes}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_comment_likes(cls, comment_id):
        _filter = {
            'comment_id': comment_id
        }
        try:
            likes = super().find(_filter)
            return {'status': True, 'likes': likes}
        except Exception as e:
            return {'status': False, 'error': e}

    def unlike(self):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}
