from typing import Union

from .table import Table


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

    @classmethod
    def send(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self, *args, **kwargs):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def find_via_pk(cls, pk: Union[str, int]) -> dict:
        try:
            post = super().find_via_pk(pk)
            return {'status': True, 'post': post}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_post_by_user_id(cls, user_id):
        _filter = {
            'user_id': user_id
        }
        try:
            posts = super().find(_filter)
            return {'status': True, 'posts': posts}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_shared_post(cls, share_id):
        _filter = {
            'share': share_id
        }
        try:
            posts = super().find(_filter)
            return {'status': True, 'posts': posts}
        except Exception as e:
            return {'status': False, 'error': e}
