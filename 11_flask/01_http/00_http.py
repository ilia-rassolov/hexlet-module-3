'''
Пейджинг — механизм, который позволяет итерироваться по большим коллекциям небольшими порциями. Часто встречается в
Интернете, например, в результатах запросов поисковых систем. Пейджинг с точки зрения пользователя выглядит как
 параметры запроса: page определяет текущую страницу, а per — количество элементов на страницу. Имена могут быть и
 другими, но обычно их называют, как показано выше. Запрос c page, равным 1, аналогичен запросу без указания page.

src/app.py
Реализуйте маршрут /companies, по которому отдается список компаний в виде json. Компании отдаются не все сразу, а
только соответствующие текущей запрошенной странице. По умолчанию выдается 5 результатов на запрос.

# выдаст первые пять компаний
GET /companies

# выдаст компании с 7 по 9
GET /companies?page=3&per=3
Подсказки
Список компаний лежит в массиве companies
При получении параметров запроса используйте type. Это позволит привести полученное значение к определенному типу
https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MultiDict.get
'''


from flask import Flask, jsonify, request


from data import generate_companies


companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"

@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    start = (page - 1) * per
    end = start + per
    return jsonify(companies[start:end])