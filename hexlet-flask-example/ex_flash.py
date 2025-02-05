'''
В этом задании вам предстоит добавить флеш-сообщения, которые позволяют сообщить пользователю о результате его действий.

src/app.py.py
Реализуйте два обработчика:

/ — выводит флеш-сообщения в шаблон templates1/index.html.
/courses — добавляет сообщение Course Added во flash и делает редирект на /.
templates1/index.html
Реализуйте вывод flash-сообщений
'''

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    render_template,
    redirect,
    url_for
)
import os



app = Flask(__name__)
# app.py.config.py['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.secret_key = 'super secret key'


# BEGIN (write your solution here)
@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    print(messages)  # => [('success', 'This is a message')]
    return render_template(
        'courses/index_flash.html',
        messages=messages,
    )


@app.post('/courses')
def course_post():
    flash('Course Added', 'success')
    return redirect('/')  # без url_for
# END

# if __name__ == "__main__":
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    # app.py.secret_key = 'super secret key'
    # app.py.config.py['SESSION_TYPE'] = 'filesystem'
    #
    # app.py.debug = True
    # app.py.run()
