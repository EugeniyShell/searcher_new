from flask import Flask, render_template, request

from .crawling import crawl_it
from .base_renew import base_renew
from .db import db, base_search
from .defs import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MOD, SOURCEPATH


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
        db.drop_all()
        db.create_all()
        base_renew()
        db.session.commit()
        return index("База обновлена!")

    @app.route("/variants", methods=['GET'])
    def variants():
        search = request.args.get('search')
        if not search:
            return index('Вы ничего не ввели, будьте внимательнее')
        search_list = base_search(search)
        if not search_list:
            return index(f'Не удалось найти "{search}", '
                         f'попробуйте другое ключевое слово')
        return render_template('variants.tpl', message=search,
                               search_list=search_list)

    @app.route("/result", methods=['POST'])
    def result():
        search_list = request.form.getlist('search')
        result_list = crawl_it(search_list)
        return render_template('result.tpl', search_list=search_list,
                               result_list=result_list)

    @app.errorhandler(404)
    def page404(_):
        return index("Нет такой страницы. Поищите ещё.")

    db.init_app(app)
    return app
