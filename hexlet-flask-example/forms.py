from flask import Flask, render_template
from flask import request

from data.data_forms import users

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/users">Users</a>'


@app.route('/users')
def find_users():
    # return 'abc'
    query = request.args.get('query', '')
    filter_users = list(filter(lambda user: query in user['name'], users))
    return render_template('index_forms.html', users=filter_users, search=query)

# print(list(filter(lambda user: 'mi' in user['name'], users)))

# if __name__ == '__main__':
#     app.run(debug=True, port=7000)
