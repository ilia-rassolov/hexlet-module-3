import json
import uuid
from flask import Flask, redirect, render_template, request, flash, get_flashed_messages

app = Flask(__name__)

users = json.load(open("data/users.json", 'r'))


@app.route('/')
def index():
    return '<a href="/users">Modifying forms</a>'

@app.route('/users/')
def users_get():
    return render_template(
        'users/index.html',
        users=users
    )

@app.post('/users')
def users_post():
    user_data = request.form.to_dict()
    errors = validate(user_data)
    if errors:
        return render_template(
            'users/new.html',
            user=user_data,
            errors=errors,
        )
    id = str(uuid.uuid4())
    user = {
        'id': id,
        'name': user_data['name'],
        'email': user_data['email']
    }
    users.append(user)
    with open("data/users.json", "w") as f:
        json.dump(users, f)
    # flash('This is a message', 'success')
    return redirect('/users', code=302)

@app.route('/users/new')
def users_new():
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors,
    )


@app.route('/users/<id>')
def show_user(id):
    with open("data/users.json", "r") as f:
        users = json.load(f)
    user = next(user for user in users if id == str(user['id']))
    return render_template(
        'users/show.html',
        user=user,
    )


def validate(user):
    errors = {}
    if not user['name']:
        errors['name'] = "Can't be blank"
    if not user['email']:
        errors['email'] = "Can't be blank"
    return errors


@app.post('/foo')
def foo_post():
    # Добавление флеш-сообщения.
    # Оно станет доступным только на следующий HTTP-запрос.
    # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
    # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
    flash('This is a message', 'success')
    return redirect('/bar')

@app.get('/bar')
def bar_index():
    # Извлечение flash-сообщений, которые установлены на предыдущем запросе
    messages = get_flashed_messages(with_categories=True)
    print(messages)  # => [('success', 'This is a message')]
    return render_template(
        'bar.html',
        messages=messages,
    )