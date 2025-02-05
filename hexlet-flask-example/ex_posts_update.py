from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from data.repo_post_cc import PostsRepository


app = Flask(__name__)
app.secret_key = "secret_key"
# app.py.config.py['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index_posts.html')

repo = PostsRepository(10)


@app.get('/posts/')
def posts_get():
    # repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index_up.html',
        posts=posts,
        messages=messages,
        )


@app.route('/posts/new')
def new_post():
    post = {}
    errors = {}
    return render_template(
        'posts/new_up.html',
        post=post,
        errors=errors,
    )


@app.post('/posts')
def posts_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new_up.html',
            post=data,
            errors=errors,
            ), 422
    id = repo.save(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id
    return resp


# BEGIN (write your solution here)
@app.route('/posts/<id>/update')
def posts_edit(id):
    # repo = PostsRepository()
    post = repo.find(id)
    errors = {}

    return render_template(
           'posts/edit.html',
           post=post,
           errors=errors,
    )

@app.route('/posts/<id>/update', methods=['POST'])
def posts_patch(id):

    post = repo.find(id)
    data_post = request.form.to_dict()
    errors = validate(data_post)
    if errors:
        return render_template(
            'posts/edit.html',
            post=post,
            errors=errors,
        ), 422
    repo.destroy(post)
    post['title'] = data_post['title']
    post['body'] = data_post['body']
    repo.save(post)
    flash('Post has been updated', 'success')
    return redirect(url_for('posts_get'))
# END

def validate(post):
    errors = {}
    if not post.get('title'):
        errors['title'] = "Can't be blank"
    if not post.get('body'):
        errors['body'] = "Can't be blank"
    return errors