from flask import Flask, render_template

from main.db import db
from main.defs import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder="../staticfiles")
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
        SQLALCHEMY_TRACK_MODIFICATIONS

    @app.route("/")
    def index(message="Превед!"):
        return render_template('index.tpl', message=message)

    @app.errorhandler(404)
    def page404(_):
        return index("Нет такой страницы. Поищите ещё.")

    # db.init_app(app)
    return app
