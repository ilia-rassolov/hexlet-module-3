'''
Большинство сайтов представляет собой набор веб-страниц, через которые пользователи взаимодействуют с
данными.
В этой практике вам предстоит выводить список пользователей, а также детальные странички каждого
 пользователя.
src/app.py
Реализуйте обработчики для вывода списка пользователей /users и конкретного пользователя /users/<id>. Список
 пользователей содержится в переменной users. Каждый пользователь представлен словарем, у которого есть
 числовой ключ id.
Пример
# Гипотетический пример показывающий структуру
users = [
  {
    'id': 4,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@gmail.com',
  },
  # другие пользователи
]
Если пользователя с таким идентификатором не существует, сайт должен вернуть ошибку 404 (страница
с HTTP кодом 404) и текстом Page not found.

src/templates1/users/index.html
Реализуйте вывод списка пользователей /users со ссылкой на просмотр каждого из них:

Список пользователей выведите в табличном виде с полями: id и first_name
first_name сделайте ссылкой на страницу конкретного пользователя
Пример
<table>
  <tr>
    ...
    <td>4</td>
    <td>
      <a href="/users/4">John</a>
    </td>
    ...
  </tr>
</table>

templates1/users/show.html
Реализуйте вывод всех полей пользователя по маршруту /users/<id>. Вывод организуйте как вам удобно —
проще всего использовать таблицу.

Подсказки
Использование цикла for в шаблонах.
https://jinja.palletsprojects.com/en/stable/templates/#for
'''

from flask import Flask, render_template

from data.data4 import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/users/"> Users </a>'


# BEGIN (write your solution here)
@app.route('/users/')
def show_users():
    return render_template('index4.html', users=users)

@app.route('/users/<int:id>')
def find_user(id: int):
    for user in users:
        if user['id'] == id:
            return render_template('users/show.html', user=user)
    return 'Page not found', 404

# END

print(users)