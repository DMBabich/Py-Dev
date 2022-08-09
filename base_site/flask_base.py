from flask import Flask
from flask import request
from flask import render_template

from hh import parcer


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
    return render_template('about.html', result=check)


if __name__ == '__main__':
    app.run(debug=True)
