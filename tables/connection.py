from typing import Union

from app import exe_query
from . import Like, Post, Comment
from .table import Table


class Connection(Table):
    _table_pk = 'id'
    _table_name = 'Connection'

    def __init__(self, data):
        self.id = data[0]
        self.user_caller_id = data[1]
        self.user_invited_id = data[2]
        self.connected = data[3]

    @classmethod
    def connect_request(cls, *args, **kwargs):
        try:
            super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def accept_request(self, user_caller_id):
        try:
            super().update_via_pk({'user_caller_id': user_caller_id}, self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_via_pk(cls, pk: Union[str, int]) -> 'dict':
        try:
            connection = super().find_via_pk(pk)
            return {'status': True, 'connection': connection}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find_user_connections(cls, user_id):
        _filter = {
            'user_invited_id': user_id,
            'user_caller_id': user_id
        }
        query = f'SELECT * from {cls._table_name} WHERE user_caller_id=? or user_invited_id=?'
        try:
            connections = exe_query(query, user_id, user_id)
            return {'status': True, 'connections': connections}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_related_posts(cls, user_id):
        res = cls.find_user_connections(user_id)
        if res.get('status'):
            connections = res.get('connections')
            res_posts = []
            try:
                for connection in connections:
                    likes: list = Like.get_user_likes(user_id).get('likes')
                    posts: list = Post.get_post_by_user_id(user_id).get('posts')
                    comments: list = Comment.get_comments_by_user_id.get('comments')
                    res_posts += posts
                    for ele in likes + comments:
                        temp_post = Post.find_via_pk(ele.post_id).get('posts')
                        res_posts.append(temp_post)

                    return {'status': True, posts: res_posts}

            except Exception as e:
                return {'status': False, 'error': e}

        else:
            return res
