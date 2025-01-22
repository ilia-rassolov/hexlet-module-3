'''
src/app.py
Добавьте обработчики для добавления нового товара и для просмотра информации о товаре:

GET запрос на адрес /products/new — отрисовка формы добавления нового товара
GET запрос на адрес /products/<id> — просмотр информации о конкретном товаре
POST запрос на адрес /products — создание нового товара
Для работы с базой используйте репозиторий
Продукт содержат два поля: title и price. Они обязательны к заполнению. Валидация уже написана, но не забудьте
про вывод ошибок валидации.

templates1/products/index.html
Реализуйте вывод списка товаров в виде таблицы. В таблице выводится title и price товара.

templates1/products/new.html
Шаблон для создания товара. Общая часть формы уже выделена в form.html, подключите ее.

Подсказки
Include
Для редиректов в обработчиках используйте именованный роутинг
'''

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from data.repo_db import get_db, ProductsRepository
from validator_db import validate
import psycopg


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

conn_ = psycopg.connect(dbname='hexlet', user='user')
repo = ProductsRepository(conn_)


@app.route('/')
def index():
    return render_template('index_db.html')


@app.route('/products')
def products():
    products = repo.get_entities()
    return render_template('products/index.html', products=products)


# BEGIN (write your solution here)
@app.route('/products/<id>')
def find_product(id):
    product = repo.find(id)
    return render_template('products/show.html', product=product)


@app.route('/products/new')
def new_product():
    return render_template('products/new.html', product={}, errors={})

@app.post('/products')
def add_product():
    product_data = request.form.to_dict()
    errors = validate(product_data)
    if errors:
        return render_template('products/new.html', errors=errors, product=product_data), 422
    repo.save(product_data)
    render_template('products/new.html', product=product_data, errors=errors), 422
    return redirect(url_for('products'))



    # END