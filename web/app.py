
from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/on')
def on():
    return send_ir('light:on')


@app.route('/off')
def off():
    return send_ir('light:off')


def send_ir(name):
    command = ['python', 'irrp.py', '-p', '-g27',
               '-f', './config/val/val.json', name]
    res = subprocess.run(command)
    if res:
        return "{'status':False}"
    else:
        return "{'status':True}"


if __name__ == "__main__":
    app.run(debug=True)
