from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/friends')
def hello_world():
    return [
        'Adil',
        'Afrid',
        'Asif',
        'Shoyab'
    ]
