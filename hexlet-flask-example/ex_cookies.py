'''
Чтобы отличить заказы одного пользователя от другого нужно привязать их к какому-то уникальному идентификатору.
 Для этого мы можем использовать механизм кук и хранить все данные заказа в браузере пользователя или как говорят,
  на клиенте.
В этой практике вам нужно будет реализовать корзину сайта с двумя обработчиками ее содержимого.

src/app.py.py
Реализуйте два обработчика:
POST /cart-items — для добавления товаров в корзину
POST /cart-items/clean — для очистки корзины
Корзина должна быть представлена сериализованным в JSON словарем и храниться на клиенте в куках. В корзине нужно
хранить наименование товара и его количество. Когда товар добавляется, это приводит к увеличению счетчика и редиректу
 на главную страницу. Если очистить корзину, это приведет к удалению всех товаров из корзины и также редиректу
 на главную страницу.
Структуру данных корзины можно посмотреть в шаблоне src/templates1/index.html.

Подсказки
Для сериализации/десериализации данных используйте json.dumps() и json.loads()
flask.redirect() возвращает объект ответа Response
Работа с Cookies https://flask.palletsprojects.com/en/stable/quickstart/#cookies
set_cookie() https://flask.palletsprojects.com/en/stable/api/#flask.Response.set_cookie
'''

from flask import Flask, json, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index_cook.html', cart=cart)


# BEGIN (write your solution here)
from flask import make_response


@app.post('/cart-items')
def add_item():
    data = request.form.to_dict()
    id_data = data['item_id']
    item_data = data['item_name']
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    if id_data not in cart:
        cart[id_data] = {"name": item_data, "count": 1}
    else:
        cart[id_data]["count"] += 1
    encoded_cart = json.dumps(cart)
    response = make_response(redirect('/'))
    response.set_cookie('cart', encoded_cart)
    return response


@app.post('/cart-items/clean')
def clean():
    # cart = json.loads(request.cookies.get('cart', json.dumps({})))
    empty_cart = json.dumps({})
    response = make_response(redirect('/'))
    response.set_cookie('cart', empty_cart)
    return response