from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
headerMenu = ["Установка Flask", "Первое приложение", "Обратная связь"]

@app.route("/")
def index():
    return render_template("index.html", title="Главная", menu=headerMenu)

@app.route('/about')
def about():
    return render_template('about.html', title="О сайте", menu=headerMenu)

