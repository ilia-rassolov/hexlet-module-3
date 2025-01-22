'''
Чтобы добавлять данные на сайте существуют POST-формы. Но перед тем как сохранить данные, их нужно провалидировать,
чтобы некорректные данные не попали в хранилище.
В этом упражнении вам предстоит добавить валидацию для формы создания курса, а также добавить вывод самой формы.

src/validator.py
Реализуйте функцию-валидатор, которая проверяет данные курса.
Валидации:
Свойство paid должно быть заполнено
Свойство title должно быть заполнено
Если поле не заполнено, то используется сообщение Can't be blank

src/app.py
Импортируйте функцию validate() из модуля validator.py
Реализуйте создание курсов, в которое входит два обработчика /courses/new (отображает форму /courses/new.html) и
 /courses создает курс.
Если данные формы валидны, то сохраните курс repo.save(course) и выполните редирект на страницу со списком курсов
 /courses. Если данные не валидны, то выведите форму с заполненными полями и сообщения об ошибках.

Подсказки
В случае ошибок валидации нужно возвращать код 422
При именовании полей в форме (аттрибут name) используйте схему, которая описана и показана в теории. Все данные формы
 должны попадать в один словарь, именем которого является имя сущности
'''

from flask import Flask, redirect, render_template, request
# BEGIN (write your solution here)
from validator import validate
# END
import os

from data.data_v import Repository


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


repo = Repository()


@app.route('/')
def index():
    return render_template('index_v.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index_v.html',
        courses=courses,
        )

# BEGIN (write your solution here)


@app.post('/courses')
def courses_post():
    course_data = request.form.to_dict()
    errors = validate(course_data)
    if errors:
        return render_template(
            'courses/new_v.html',
            course=course_data,
            errors=errors
        ), 422
    repo.save(course_data)
    return redirect('/courses', code=302)


@app.route('/courses/new')
def course_new():
    course = {'title': '', 'paid': ''}
    errors = {}
    return render_template(
        'courses/new_v.html',
        course=course,
        errors=errors,
    )

# END
