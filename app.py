from flask import  Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/blog')
def blog():
    return 'Ini blog'


app.run('0.0.0.0', debug=True)