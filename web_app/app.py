from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Flask-01')

    @app.route('/blog')
    def blog():
        return 'Ini blog'

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='About me')

    return app
