from typing import Union

from dns.resolver import query

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
        res_posts = []
        connections = cls.find_user_connections(user_id).get('connections')
        try:
            # for connection in connections:
            #     connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
            #     likes: list = Like.get_user_likes(connect_user_id).get('likes')
            #     posts: list = Post.get_post_by_user_id(connect_user_id).get('posts')
            #     comments: list = Comment.get_comments_by_user_id(connect_user_id).get('comments')
            #     res_posts += posts
            #     for ele in likes + comments:
            #         if ele.post_id:
            #             temp_post = Post.find_via_pk(ele.post_id).get('post')
            #             res_posts.append(temp_post)
            query1 = f'SELECT * FROM Connection WHERE Connection.user_caller_id = ?'
            query2 = f'SELECT user.* FROM user JOIN ({query1}) ON user.id = user_invited_id'
            query3 = f'SELECT Post.* FROM Post JOIN ({query2}) as U WHERE Post.user_id == U.id'
            query4 = f'SELECT Like.* FROM Like JOIN ({query2}) as U  ON Like.user_id = U.id'
            query5 = f'SELECT Post.* FROM POST JOIN ({query4}) ON post_id = Post.id'
            query6 = f'SELECT Comment.* FROM Comment JOIN ({query2}) as U  ON Comment.user_id = U.id'
            query7 = f'SELECT Post.* FROM POST JOIN ({query6}) ON post_id = Post.id'

            query8 = f'SELECT * FROM Connection WHERE Connection.user_invited_id = ?'
            query9 = f'SELECT user.* FROM user JOIN ({query8}) ON user.id = user_caller_id'
            query10 = f'SELECT Post.* FROM Post JOIN ({query9}) as U WHERE Post.user_id == U.id'
            query11 = f'SELECT Like.* FROM Like JOIN ({query9}) as U  ON Like.user_id = U.id'
            query12 = f'SELECT Post.* FROM POST JOIN ({query11}) ON post_id = Post.id'
            query13 = f'SELECT Comment.* FROM Comment JOIN ({query9}) as U  ON Comment.user_id = U.id'
            query14 = f'SELECT Post.* FROM POST JOIN ({query13}) ON post_id = Post.id'

            final_query = f'{query3} UNION {query5} UNION {query7} UNION {query10} UNION {query12} UNION {query14}'
            res_posts = [Post(post) for post in exe_query(final_query, *[user_id] * 6)]

            return {'status': True, "posts": res_posts}


        except Exception as e:
            return {'status': False, 'error': e}

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
    def mutual_connection_number(cls, user1_id, user2_id):
        try:
            # user2_connections = cls.find_user_connections(user2_id).get('connections')
            # mutual = 0
            # for user2_connection in user2_connections:
            #     connect_user_id = user2_connection.user_caller_id if user2_connection.user_caller_id != user2_id \
            #         else user2_connection.user_invited_id
            #
            #     if cls.get_connect_with_users_id(user1_id, connect_user_id).get('connection'):
            #         mutual += 1
            test = []
            query1 = f'SELECT user_invited_id as id FROM Connection WHERE user_caller_id = ? and user_invited_id != ? and connected = ?'
            query2 = f'SELECT user_caller_id as id FROM Connection WHERE user_invited_id = ? and user_caller_id != ? and connected = ?'
            query3 = f'SELECT id FROM ({query1}) WHERE id IN ({query1})'
            test += exe_query(query3, *[user1_id, user2_id, True, user2_id, user1_id, True])

            query4 = f'SELECT id FROM ({query1}) WHERE id IN ({query2})'
            test += exe_query(query4, *[user1_id, user2_id, True, user2_id, user1_id, True])

            query5 = f'SELECT id FROM ({query2}) WHERE id IN ({query1})'
            test += exe_query(query5, *[user1_id, user2_id, True, user2_id, user1_id, True])

            query6 = f'SELECT id FROM ({query2}) WHERE id IN ({query2})'
            test += exe_query(query6, *[user1_id, user2_id, True, user2_id, user1_id, True])

            final_query = f'SELECT DISTINCT COUNT(id) FROM ({query3} UNION {query4} UNION {query5} UNION {query6})'
            mutual = exe_query(final_query, *[user1_id, user2_id, True, user2_id, user1_id, True] * 4)[-1][-1]

            return {'status': True, 'mutual': mutual}
        except Exception as e:
            return {'status': False, 'error': e}

    @classmethod
    def search_connection(cls, **kwargs):
        user_id = kwargs.get('user_id')
        username = kwargs.get('username')
        language = kwargs.get('language')
        location = kwargs.get('location')
        experience = kwargs.get('experience')
        args = []
        username_query, language_query, location_query, experience_query = '', '', '', ''
        if username:
            username = f'%{username}%'
            query1 = f'SELECT id, user_caller_id, user_invited_id, connected FROM (SELECT * FROM {cls._table_name} JOIN user ' \
                     f'ON user.id = {cls._table_name}.user_caller_id ' \
                     f'and {cls._table_name}.user_invited_id = ?) WHERE username LIKE ?'

            query2 = f'SELECT id, user_caller_id, user_invited_id, connected FROM (SELECT * FROM {cls._table_name} JOIN user ' \
                     f'ON user.id = {cls._table_name}.user_invited_id ' \
                     f'and {cls._table_name}.user_caller_id = ?) WHERE username LIKE ?'
            args += [user_id, username, user_id, username]
            username_query = f'{query1} UNION {query2}'

        if language:
            language = f'%{language}%'
            query1 = f'''SELECT id, user_caller_id, user_invited_id, connected FROM
            (SELECT UC.id, UC.user_caller_id, UC.user_invited_id, UC.connected, Language.language FROM 
            (SELECT * FROM {cls._table_name} JOIN user 
            ON user.id = {cls._table_name}.user_invited_id 
            and {cls._table_name}.user_caller_id = ?) as UC JOIN Language ON UC.user_invited_id = Language.user_id) WHERE language LIKE ?'''

            query2 = f'''SELECT id, user_caller_id, user_invited_id, connected FROM
            (SELECT UC.id, UC.user_caller_id, UC.user_invited_id, UC.connected, Language.language FROM 
            (SELECT * FROM {cls._table_name} JOIN user 
            ON user.id = {cls._table_name}.user_caller_id 
            and {cls._table_name}.user_invited_id = ?) as UC JOIN Language ON UC.user_caller_id = Language.user_id) WHERE language LIKE ?'''
            language_query = f'{query1} UNION {query2}'
            args += [user_id, language, user_id, language]
        if location:
            location = f'%{location}%'
            query1 = f'SELECT id, user_caller_id, user_invited_id, connected FROM (SELECT * FROM {cls._table_name} JOIN user ' \
                     f'ON user.id = {cls._table_name}.user_caller_id ' \
                     f'and {cls._table_name}.user_invited_id = ?) WHERE nationality LIKE ?'

            query2 = f'SELECT id, user_caller_id, user_invited_id, connected FROM (SELECT * FROM {cls._table_name} JOIN user ' \
                     f'ON user.id = {cls._table_name}.user_invited_id ' \
                     f'and {cls._table_name}.user_caller_id = ?) WHERE nationality LIKE ?'
            args += [user_id, location, user_id, location]
            location_query = f'{query1} UNION {query2}'

        if experience:
            experience = f'%{experience}%'
            query1 = f'''SELECT id, user_caller_id, user_invited_id, connected FROM
            (SELECT UC.id, UC.user_caller_id, UC.user_invited_id, UC.connected, Experience.text, Experience.end_time FROM 
            (SELECT * FROM {cls._table_name} JOIN user 
            ON user.id = {cls._table_name}.user_invited_id 
            and {cls._table_name}.user_caller_id = ?) as UC JOIN Experience ON UC.user_invited_id = Experience.user_id) WHERE text LIKE ? 
            and end_time IS NULL '''

            query2 = f'''SELECT id, user_caller_id, user_invited_id, connected FROM
            (SELECT UC.id, UC.user_caller_id, UC.user_invited_id, UC.connected, Experience.text, Experience.end_time FROM 
            (SELECT * FROM {cls._table_name} JOIN user 
            ON user.id = {cls._table_name}.user_caller_id 
            and {cls._table_name}.user_invited_id = ?) as UC JOIN Experience ON UC.user_caller_id = Experience.user_id) WHERE text LIKE ?
            and end_time IS NULL'''
            experience_query = f'{query1} UNION {query2}'
            args += [user_id, experience, user_id, experience]
        if args:
            try:
                final_query = ''
                for _query in username_query, location_query, language_query, experience_query:
                    if _query:
                        final_query += f'{_query} INTERSECT '
                final_query = final_query.removesuffix('INTERSECT ')
                res = [Connection(connection) for connection in exe_query(final_query, *args)]
                return {'status': True, 'connections': res}
            except Exception as e:
                return {'status': False, 'error': e}

        else:
            return Connection.find_user_connections(user_id)
