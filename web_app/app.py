from flask import Flask, render_template
import psycopg2

from web_app.models import db, Page


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    @app.route('/')
    def index():
        page = Page.query.filter_by(id=1).first()
        return render_template('index.html', TITLE='Flask-01', CONTENT=page.contents)

    @app.route('/blog')
    def blog():
        return 'Ini blog'

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='About me')

    @app.route('/testdb')
    def testdb():
        con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
        cur = con.cursor()
        cur.execute('select * from page;')

        id, contents = cur.fetchone()
        con.close()
        return 'Output DB: {} - {}'.format(id, contents)

    return app
