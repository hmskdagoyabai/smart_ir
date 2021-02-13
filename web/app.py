
from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello():
    return '<a href="/on">on</a><br><a href="/off">off</a>'


@app.route('/on')
def on():
    return send_ir('light:on')


@app.route('/off')
def off():
    return send_ir('light:off')


def send_ir(name):
    command = ['python', 'irrp.py', '-p', '-g27',
               '-f', './config/val/val.json', name]
    res = subprocess.call(command)
    if res:
        return "{'status':False}"
    else:
        return "{'status':True}"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
