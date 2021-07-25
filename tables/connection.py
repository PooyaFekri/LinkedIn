from typing import Union

from app import exe_query
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
        connection = cls.get_connect_with_users_id(kwargs['user_caller_id'], kwargs['user_invited_id']).get(
            'connection')
        try:
            if not connection:
                super().insert(kwargs)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    def accept_request(self):
        try:
            super().update_via_pk({'connected': True}, self.id)
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

    # TODO : See all function called
    @classmethod
    def find_user_connections(cls, user_id):
        _filter = {
            'user_invited_id': user_id,
            'user_caller_id': user_id
        }
        query = f'SELECT * from {cls._table_name} WHERE connected=? and (user_caller_id=? or user_invited_id=?)'
        try:
            connections = [Connection(connection) for connection in exe_query(query, 1, user_id, user_id)]
            return {'status': True, 'connections': connections}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_related_posts(cls, user_id):
        from . import Like, Post, Comment
        res = cls.find_user_connections(user_id)
        if res.get('status'):
            connections = res.get('connections')
            res_posts = []
            try:
                for connection in connections:
                    connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                    likes: list = Like.get_user_likes(connect_user_id).get('likes')
                    posts: list = Post.get_post_by_user_id(connect_user_id).get('posts')
                    comments: list = Comment.get_comments_by_user_id(connect_user_id).get('comments')
                    res_posts += posts
                    for ele in likes + comments:
                        if ele.post_id:
                            temp_post = Post.find_via_pk(ele.post_id).get('post')
                            res_posts.append(temp_post)

                    return {'status': True, "posts": res_posts}

            except Exception as e:
                return {'status': False, 'error': e}

        else:
            return res

    @classmethod
    def is_connected(cls, user1_id, user2_id):
        try:
            connection = cls.get_connect_with_users_id(user1_id, user2_id).get('connection')
            return {'status': True, 'is_connected': bool(connection) and connection.connected}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def find(cls, *args, **kwargs):
        try:
            connections = super().find(kwargs)
            return {'status': True, 'connections': connections}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def get_connect_with_users_id(cls, user1_id, user2_id):
        _filter1 = {
            'user_invited_id': user1_id,
            'user_caller_id': user2_id
        }

        _filter2 = {
            'user_invited_id': user2_id,
            'user_caller_id': user1_id
        }
        try:
            connection = super().find(_filter1) + super().find(_filter2)

            return {'status': True, 'connection': connection[-1]}
        except Exception as e:
            return {'status': False, 'error': e}

    def delete(self):
        try:
            super().delete_via_pk(self.id)
            return {'status': True}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def search_connection(cls, *args, **kwargs):
        from . import User, Language, Experience
        user_id = kwargs['user_id']
        connections = cls.find_user_connections(user_id).get('connections')
        res_connections = []
        my_user = User.find_via_pk(user_id).get('user')
        try:
            for connection in connections:
                connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                user = User.find_via_pk(connect_user_id).get('user')
                flag = 1
                if username := kwargs.get('username'):
                    search_by_username = my_user.search(username).get('users')
                    for searched_user in search_by_username:
                        if user.username == searched_user.username:
                            flag = 1
                            break
                        else:
                            flag = 0
                if location := kwargs.get('location'):
                    if user.nationality != location:
                        continue
                if lang := kwargs.get('language'):
                    languages = Language.find_user_lang(connect_user_id).get('languages')
                    if not languages:
                        flag = 0
                        break
                    for language in languages:
                        if language.language != lang:
                            flag = 0
                        else:
                            flag = 1
                            break
                if exp := kwargs.get('experience'):
                    experiences = Experience.find_user_experiences(connect_user_id).get('experiences')
                    if not experiences:
                        continue
                    for experience in experiences:
                        if exp != experience.text and not experience.end_time:
                            flag = 1
                            break
                        else:
                            flag = 0
                if flag:
                    res_connections.append(connection)

            return {'status': True, 'connections': res_connections}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def mutual_connection_number(cls, user1_id, user2_id):
        try:
            user1_connections = cls.find_user_connections(user1_id).get('connections')
            user2_connections = cls.find_user_connections(user2_id).get('connections')
            mutual = 0
            for user2_connection in user2_connections:
                connect_user_id = user2_connection.user_caller_id if user2_connection.user_caller_id != user2_id \
                    else user2_connection.user_invited_id

                if cls.get_connect_with_users_id(user1_id, connect_user_id).get('connection'):
                    mutual += 1

            return {'status': True, 'mutual': mutual}
        except Exception as e:
            return {'status': False, 'error': e}
