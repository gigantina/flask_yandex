from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return '''Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!'''


@app.route('/image_mars')
def image():
    return '''<h1>Жди нас, Марс!</h1><img src="/static/images/mars.jpg" alt="здесь должна была быть картинка, но не нашлась" width = "30%"><br>Вот он, сон Маска'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
