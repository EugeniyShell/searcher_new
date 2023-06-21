from flask import Flask, render_template

from main.base_renew import base_renew
from main.db import db
from main.defs import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MOD, SOURCEPATH


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder="../staticfiles")
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MOD

    @app.route("/")
    def index(message="Начинаем поиск?"):
        return render_template('index.tpl', message=message)

    @app.route("/renew")
    def renew():
        base_renew()
        return index("База обновлена!")

    @app.errorhandler(404)
    def page404(_):
        return index("Нет такой страницы. Поищите ещё.")

    db.init_app(app)
    return app
