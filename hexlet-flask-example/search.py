"""
Ни один сайт не обходится без поисковой строки. Зачастую, поиск работает по принципу приближенного соответствия строк.
В этом упражнении вам нужно будет создать форму для поиска имени пользователя, которое начинается с введенных букв.

src/app.py
Реализуйте обработчик по маршруту /users, который формирует список пользователей. Обработчик поддерживает фильтрацию
через параметр term, в котором передается first_name. Он возвращает все совпадения по началу имени пользователя.
Список пользователей доступен в переменной users.

src/templates1/users/index.html
Реализуйте вывод списка пользователей и формы для фильтрации.
Если форма пустая, то должен выводиться список всех пользователей. Если заполнена, то отфильтрованный по совпадениям.
Поле ввода должно сохранять введенное значение.
Примечания
Поиск должен быть регистронезависимым
"""

from flask import Flask, render_template, request
import re
from flask import make_response

from data.data4 import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('index.html')
    return '<a href="/users">Users</a>'


# BEGIN (write your solution here)
@app.route('/users')
def find_users():
    term = request.args.get('term', '')
    filter_users = list(filter(lambda user: re.search(f"(?i:\A{term})", user['first_name']), users))
    new_users = filter_users if filter_users else users
    # names_users = []
    # for user in users:
    #     name_user_lower = user['first_name'].lower()
    #     length = len(term)
    #     if name_user_lower[:length] == term:
    #         names_users.append(user['first_name'])
    return render_template('index_forms.html', users=new_users, search=term)

# END
# query = 'Mi'
# user = 'misha'
# print(re.search(f"(?i:\A{query})", user))
# query = 'mi'
# print(list(filter(lambda user: re.search(f"(?i:\A{query})", user['first_name']), users)))
