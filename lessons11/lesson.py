from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return 'Hello World! {}'.format(username)

def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()