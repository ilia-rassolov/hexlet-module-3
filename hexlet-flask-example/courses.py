from flask import Flask, render_template
from data.data_courses import generate_courses


app = Flask(__name__)

all_courses = generate_courses(100)


@app.route('/')
def index():
    return '<a href="/courses">Курсы</a>' '              ' '<a href="/courses/index">Индекс</a>'


@app.route('/courses')
def show_courses():
    return render_template('/courses/layout.html')

@app.route('/courses/<int:id>')
def find_user(id: int):
    for course in all_courses:
        if course['id'] == id:
            return render_template('courses/show_c.html', course=course)
    return 'Page not found', 404

@app.route('/courses/index')
def show_child():
    return render_template('/courses/index.html', courses=all_courses)