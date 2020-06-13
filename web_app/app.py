from flask import  Flask
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello Flask'

    @app.route('/blog')
    def blog():
        return 'Ini blog'

    return app