from random import choice

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    luck_msg = choice([
        'Вам сегодня повезет!',
        'Вам сегодня НЕ повезет!',
        'Уходи с моего сайта, Иноагент!',
    ])
    luck_msg = f'<strong>{luck_msg}</strong>'
    return render_template('index.html', luck=luck_msg)


app.run('localhost', 5000, debug=True)
