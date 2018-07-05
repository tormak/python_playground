from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/<test_name>')
def hello_name(test_name):
    return 'Hello, %s' % test_name
