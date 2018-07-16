from flask import Flask
from flask import request

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/')
def hello():
    return 'hello world'


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


app.run(host='0.0.0.0', port=5000)
