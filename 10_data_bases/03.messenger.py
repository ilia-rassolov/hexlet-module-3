import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor, DictRow, NamedTupleCursor


conn = psycopg2.connect(dbname='hexlet', user='user')


def create_post(conn, post):
    with conn.cursor() as curs:
        query = """
        INSERT INTO posts (title, content, author_id) VALUES (%(title)s, %(content)s, %(author_id)s) RETURNING id;"""
        curs.execute(query, post)
        post_id = curs.fetchone()[0]
        conn.commit()
        return post_id


def add_comment(conn, comment):
    with conn.cursor() as curs:
        query = """
        INSERT INTO comments (post_id, content, author_id) VALUES (%(post_id)s, %(content)s, %(author_id)s) RETURNING id;"""
        curs.execute(query, comment)
        comment_id = curs.fetchone()[0]
        conn.commit()
        return comment_id


def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=RealDictCursor) as curs_posts:
        query_posts = "SELECT * FROM posts ORDER BY created_at DESC;"
        curs_posts.execute(query_posts)
        posts = curs_posts.fetchmany(size=n)
        n_posts = []
        for row in posts:
            post = {}
            for pair in row:
                post[pair] = row[pair]
            post_current_id = post['id']
            with conn.cursor(cursor_factory=RealDictCursor) as curs_comments:
                query_comments = "SELECT * FROM comments WHERE post_id=%s;"
                curs_comments.execute(query_comments, (post_current_id,))
                all_comments = []
                response = curs_comments.fetchall()
                for row in response:
                    comment = {}
                    for pair in row:
                        if pair != 'post_id':
                            comment[pair] = row[pair]
                    all_comments.append(comment)
                post['comments'] = all_comments
            n_posts.append(post)
        return n_posts

# sql = """CREATE TABLE posts (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     content TEXT NOT NULL,
#     author_id INTEGER NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );"""

# with conn:
#     with conn.cursor() as curs:
#         curs.execute(sql)

post = {'title': 'My Second Post', 'content': 'text too', 'author_id': 44}
comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}

# create_post(conn, post)

# sql = """
#
# SELECT * FROM posts;
# SELECT * FROM comments;"""
# with conn:
#     with conn.cursor() as curs:
#         curs.execute(sql)
# conn.commit()
#         print(curs.fetchall())

# add_comment(conn, comment)
# with conn.cursor() as curs:
#     curs.execute("SELECT * FROM posts;")
#     print(curs.fetchall())
print(get_latest_posts(conn, 3))

conn.close()