import uuid
from data.repo_users import UsersRepository
from flask import (
    get_flashed_messages,
    flash,
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

app = Flask(__name__)
app.secret_key = "secret_key"

repo = UsersRepository()
users = repo.content()


@app.route('/')
def index():
    return '<a href="/users">Users</a>'


@app.route('/users/')
def users_index():
    messages = get_flashed_messages(with_categories=True)
    return render_template('users/index.html', users=users, messages=messages)


@app.route('/users/new')
def users_new():
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template(
        'users/new_cc.html',
        user=user,
        errors=errors,
    )


@app.route('/users/<id>')
def users_show(id):
    user = next(user for user in users if id == str(user['id']))
    if not user:
        return 'Page not found', 404
    return render_template('users/show.html', user=user,)


@app.post('/users')
def users_post():
    user_data = request.form.to_dict()
    errors = validate(user_data)
    if errors:
        return render_template(
            'users/new_cc.html',
            user=user_data,
            errors=errors,
        ), 422
    repo.save(user_data)
    flash('User added successfully', 'success')
    return redirect(url_for('users_index'), code=302)


def validate(user):
    errors = {}
    if len(user['name']) < 5:
        errors['name'] = "Name must be grater than 4 characters"
    if not user['email']:
        errors['email'] = "Can't be blank"
    return errors
#
#
# @app.py.post('/foo')
# def foo_post():
#     # Добавление флеш-сообщения.
#     # Оно станет доступным только на следующий HTTP-запрос.
#     # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
#     # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
#     flash('This is a message', 'success')
#     return redirect('/bar')
#
# @app.py.get('/bar')
# def bar_index():
#     # Извлечение flash-сообщений, которые установлены на предыдущем запросе
#     messages = get_flashed_messages(with_categories=True)
#     print(messages)  # => [('success', 'This is a message')]
#     return render_template(
#         'bar.html',
#         messages=messages,
#     )

