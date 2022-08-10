from flask import Flask
from flask import request
from flask import render_template

from hh import parcer
from tools import add_row


app = Flask(__name__)


@app.get('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/')
def form():
    return render_template('form.html')


@app.post('/result/')
def result():
    phrase = request.form
    data = parcer(**phrase)
    check = {**data, **phrase}
    print(check)
    check['where'] = 'в названии вакансии' \
        if check['where'] == 'name' else 'в названии компании' if check['where'] == 'company' else 'везде'
    add_row(check)
    return render_template('about.html', result=check)


if __name__ == '__main__':
    app.run(debug=True)
