from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
headerMenu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
def index():
    return render_template("index.html", title="Главная", menu=headerMenu)

@app.route('/about')
def about():
    return render_template('about.html', title="О сайте", menu=headerMenu)

@app.route("/install-flask")
def installFlask():
    return render_template("install_flask.html", title="Установка", menu=headerMenu)

@app.route("/first-app")
def firstApp():
    return render_template("first_app.html", title="Первое приложение", menu=headerMenu)

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Обратная связь", menu=headerMenu)