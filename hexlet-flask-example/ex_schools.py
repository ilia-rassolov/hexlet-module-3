import json
import uuid
from flask import (
    get_flashed_messages,
    flash,
    Flask,
    redirect,
    render_template,
    request,
    url_for
)
from data.repo_schools import SchoolRepository

app = Flask(__name__)
app.secret_key = "secret_key"

schools = json.load(open("data/schools.json", 'r'))


@app.route('/')
def index():
    return '<a href="/schools">Schools</a>'

@app.route('/schools/')
def schools_index():
    return render_template(
        'schools/index.html',
        schools=schools
    )


@app.route('/schools/<id>')
def schools_show(id):
    with open("data/schools.json", "r") as f:
        schools = json.load(f)
    school = next(school for school in schools if id == str(school['id']))

    if not school:
        return 'Page not found', 404

    return render_template(
        'schools/show.html',
        school=school,
    )


@app.route('/schools/<id>/edit')
def schools_edit(id):
    repo = SchoolRepository()
    school = repo.find(id)
    errors = {}

    return render_template(
           'schools/edit.html',
           school=school,
           errors=errors,
    )

@app.route('/schools/<id>/patch', methods=['POST'])
def schools_patch(id):
    repo = SchoolRepository()
    school = repo.find(id)
    data_school = request.form.to_dict()
    errors = validate(data_school)
    if errors:
        return render_template(
            'schools/edit.html',
            school=school,
            errors=errors,
        ), 422

    # Ручное копирование данных из формы в нашу сущность
    school['name'] = data_school['name']
    repo.save(school)
    flash('School has been updated', 'success')
    return redirect(url_for('schools_index'))


@app.route('/schools/<id>/delete', methods=['POST'])
def schools_delete(id):
    repo = SchoolRepository()
    repo.destroy(id)
    flash('School has been deleted', 'success')
    return redirect(url_for('schools_index'))
#
# @app.post('/schools')
# def users_post():
#     user_data = request.form.to_dict()
#     errors = validate(user_data)
#     if errors:
#         return render_template(
#             'users/new.html',
#             user=user_data,
#             errors=errors,
#         )
#     id = str(uuid.uuid4())
#     user = {
#         'id': id,
#         'name': user_data['name'],
#         'email': user_data['email']
#     }
#     users.append(user)
#     with open("data/users.json", "w") as f:
#         json.dump(users, f)
#     # flash('This is a message', 'success')
#     return redirect('/users', code=302)
#
# @app.route('/users/new')
# def users_new():
#     user = {'name': '', 'email': ''}
#     errors = {}
#     return render_template(
#         'users/new.html',
#         user=user,
#         errors=errors,
#     )
#
#
#
#
#
def validate(school):
    errors = {}
    if not school['name']:
        errors['name'] = "Can't be blank"
    return errors
#
#
# @app.post('/foo')
# def foo_post():
#     # Добавление флеш-сообщения.
#     # Оно станет доступным только на следующий HTTP-запрос.
#     # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
#     # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
#     flash('This is a message', 'success')
#     return redirect('/bar')
#
# @app.get('/bar')
# def bar_index():
#     # Извлечение flash-сообщений, которые установлены на предыдущем запросе
#     messages = get_flashed_messages(with_categories=True)
#     print(messages)  # => [('success', 'This is a message')]
#     return render_template(
#         'bar.html',
#         messages=messages,
#     )

print(schools)