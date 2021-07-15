from .table import Table


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

    @classmethod
    def create(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_comments_by_user_id(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            comments = super().find(_filter)
            return {'status': True, 'comments': comments}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_comments_by_post_id(cls, post_id, *args, **kwargs):
        _filter = {
            'post_id': post_id
        }
        try:
            comments = super().find(_filter)
            return {'status': True, 'comments': comments}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_replies_comment(cls, comment_id):
        _filter = {
            'comment_reply_id': comment_id
        }
        try:
            comments = super().find(_filter)
            return {'status': True, 'comments': comments}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self, *args, **kwargs):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}
