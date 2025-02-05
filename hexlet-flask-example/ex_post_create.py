'''
В этой практике вам предстоит попрактиковаться в CREATE операций CRUD. Чтобы добавить данные используется форма
создания ресурса. Также введенные данные обязательно нужно провалидировать, чтобы в хранилище не попала некорректная
информация.

src/app.py.py
Реализуйте следующие обработчики:
Форма создания нового поста: GET /posts/new
Создание поста: POST /posts
Посты содержат два поля: title и body. Они обязательны к заполнению. Валидация уже написана, но не забудьте про
 вывод ошибок валидации.
После каждого успешного действия нужно добавлять флеш-сообщение 'Post has been created' и выводить его на списке постов.

templates1/posts/new.html
Форма для создания поста
Подсказки
Чтобы работать с репозиторием в обработчике, его нужно инициализировать по примеру в posts_get()
Чтобы сохранить пост, используйте метод репозитория save()
Для обработки незаполненных полей можно воспользоваться встроенным в шаблонизатор фильтром default()
https://jinja.palletsprojects.com/en/stable/templates/#jinja-filters.default
'''


import os

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
from data.repo_post_cc import PostsRepository
from validator_posts import validate


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index_posts.html')


@app.route('/posts/')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index_cc.html',
        posts=posts,
        messages=messages,
        )


# BEGIN (write your solution here)
@app.get('/posts/new')
def posts_create():
    post = {}
    errors = {}
    return render_template(
        'posts/new.html',
        post=post,
        errors=errors,
    )


@app.post('/posts')
def posts_post():
    post_data = request.form.to_dict()
    errors = validate(post_data)
    if errors:
        return render_template(
            'posts/new.html',
            post=post_data,
            errors=errors,
        ), 422
    repo = PostsRepository()
    repo.save(post_data)
    flash('Post has been created', 'success')
    return redirect(url_for('posts_get'), code=302)
# END