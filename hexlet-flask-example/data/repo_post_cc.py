# import json
# import sys
import uuid
# from flask import session
#
#
# class PostsRepository():
#     def __init__(self):
#         if 'posts' not in session:
#             session['posts'] = {}
#
#     def content(self):
#         return session['posts'].values()
#
#     def find(self, id):
#         try:
#             return session['posts'][id]
#         except KeyError:
#             sys.stderr.write(f'Wrong post id: {id}')
#             raise
#
#     def destroy(self, id):
#         del session['posts'][id]
#
#     def save(self, post):
#         if not (post.get('title') and post.get('body')):
#             raise Exception(f'Wrong data: {json.loads(post)}')
#         if not post.get('id'):
#             post['id'] = str(uuid.uuid4())
#         session['posts'][post['id']] = post
#         session['posts'] = session['posts']
#         return post['id']
from os import remove

from faker import Faker


fake = Faker()
Faker.seed(1234)


def generate(size):
    posts = []
    for _ in range(size):
        posts.append({
            'id': fake.uuid4(),
            'title': fake.sentence(),
            'body': fake.text(),
            })
    return posts


class PostsRepository:
    def __init__(self, size=5):
        self.posts = generate(size)

    def content(self):
        return self.posts

    def find(self, id):
        return next((post for post in self.posts if id == post['id']), None)

    def destroy(self, post):
        self.posts.remove(post)

    def save(self, post):
        if not (post.get('title') and post.get('body')):
            raise Exception(f'Wrong data: {post}')
        if not post.get('id'):
            post['id'] = str(uuid.uuid4())
        self.posts.append(post)
        return post['id']