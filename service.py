import flask
from flask import request

import os

server = flask.Flask(__name__)
server.config["DEBUG"] = False

@server.route('/', methods=["GET"])

def home():
    return "<h1>API</h1><p>This site is a prototype API.</p>"


@server.route('/stop', methods=['GET'])
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@server.route('/teste', methods=['GET'])
def teste():
    os.system('echo Hello World!')
    return home()

server.run(host='0.0.0.0', port=8080)

