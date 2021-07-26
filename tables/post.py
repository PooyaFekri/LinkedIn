from typing import Union

from app import exe_query
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
        self.is_featured = data[6]

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

    @classmethod
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

    def change_featured(self, status):
        data = {'is_featured': status}
        try:
            super().update_via_pk(data, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_featured_posts(cls, user_id):
        _filter = {
            'user_id': user_id,
            'is_featured': True
        }
        try:
            posts = super().find(_filter)
            return {'status': True, 'posts': posts}
        except Exception as e:
            return {'status': False, 'error': e}

    def get_like_number(self):
        query = f'SELECT COUNT(id) FROM Like WHERE Like.post_id = ?'
        try:
            like_number = exe_query(query, self.id)[-1][-1]
            return {'status': True, 'like_number': like_number}
        except Exception as e:
            return {'status': False, 'error': e}

    def get_comment_number(self):
        query = f'SELECT COUNT(id) FROM Comment WHERE Comment.post_id = ?'
        try:
            like_number = exe_query(query, self.id)[-1][-1]
            return {'status': True, 'comment_number': like_number}
        except Exception as e:
            return {'status': False, 'error': e}
