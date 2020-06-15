from flask import Flask, render_template
import psycopg2


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
        cur = con.cursor()
        cur.execute('select contents from page where id = 1;')

        contents = cur.fetchone() #mengembalikan tupple.
        con.close()
        return render_template('index.html', TITLE='Flask-01', CONTENT=contents[0])

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

        id, title = cur.fetchone()
        con.close()
        return 'Output DB: {} - {}'.format(id, title)

    return app
