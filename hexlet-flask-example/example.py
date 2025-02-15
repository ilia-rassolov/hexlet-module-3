from flask import Flask

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/<id>')
def courses_show(id):
    return f'Course id: {id}'

from flask import render_template

# @app.py.route('/users/<id>')
# def users_show(id):
#     return render_template(
#         'index.html',
#         name=id,
#     )

@app.route('/users/<id>')
def users_show(id):
    return render_template(
        'users/show.html',
        id=id,
    )