'''
В этой практике вам предстоит попрактиковаться в части READ операций CRUD. Обычно "чтение" предполагает вывод всей
категории ресурсов (списка пользователей, постов, комментариев) и детальный вывод конкретного ресурса (личная страничка
 пользователя). Для удобства также используется пейджинг с переходами "вперед" и "назад".

src/app.py.py
Реализуйте следующие обработчики:
Список постов: /posts
Конкретный пост /posts/<slug>, например, /posts/python-flask-crude-exercise
Посты находятся в репозитории repo. Каждый пост содержит внутри себя четыре поля:
id
title — имя поста
body — содержание поста
slug — слаг
Каждый пост из списка ведет на страницу конкретного поста. Список нужно вывести с пейджингом по пять постов на странице.
 На первой странице — первые пять постов, на второй — вторые пять и так далее. Переключение между страницами нужно
 сделать с помощью двух ссылок: назад и вперед. То, какая сейчас страница открыта, определяется параметром page.
 По умолчанию загружается первая страница.
Страница конкретного поста отображает данные поста и позволяет вернуться на список. Если поста нет, то обработчик
 должен вернуть код ответа 404 и текст 'Page not found'.

templates1/posts/index.html
Выведите список постов. Для каждого поста также нужно вывести ссылку, которая ведет на отображение — show.
Ссылка представлена в виде слага. Не забудьте также добавить блок с переключением страниц.

templates1/posts/show.html
Вывод информации о конкретном посте. Выводить только имя и содержимое поста.

Подсказки
Для реализации пейджинга понадобится извлечь все посты из репозитория с помощью метода content()
Переход между страницами реализуется с помощью параметра запроса ?page=
If Expresion
Для поиска поста по slug используйте метод репозитория find()
'''


from flask import Flask, redirect, render_template, request, flash, get_flashed_messages
from data.repo_posts import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)
posts = repo.content()


@app.route('/')
def index():
    return render_template('index_posts.html')

@app.route('/posts/')
def posts_index():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    start = (page - 1) * per
    end = start + per
    posts_next = posts[start:end]

    next_page = page + 1
    prev_page = page - 1 if page > 1 else None

    return render_template(
        'posts/index.html',
        posts=posts_next,
        next_page=next_page,
        prev_page=prev_page,
    )


@app.route('/posts/<slug>')
def posts_show(slug):
    post = repo.find(slug)
    if not post:
        return 'Page not found', 404
    return render_template(
        'posts/show.html',
        post=post,
    )
