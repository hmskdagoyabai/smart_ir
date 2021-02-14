
from flask import Flask, jsonify, redirect, render_template
import subprocess
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    # return '<a href="/on_button">on</a><br><a href="/off_button">off</a><br><a href="/on" onclick="return false;">on</a>'
    return render_template('index.html')


@app.route('/on')
def on():
    res = send_ir('light:on')
    if res:
        return jsonify({'status': False})
    else:
        return jsonify({'status': True})


@app.route('/off')
def off():
    res = send_ir('light:off')
    if res:
        return jsonify({'status': False})
    else:
        return jsonify({'status': True})


@app.route("/send/<name>")
def archive(name=""):
    if name == "":
        return jsonify({'status': False})
    else:
        res = send_ir(name)

        if res:
            return jsonify({'status': False})
        else:
            return jsonify({'status': True})


def send_ir(name):
    command = ['python', 'irrp.py', '-p', '-g27',
               '-f', './config/val/val.json', name]
    res = subprocess.call(command)
    return res


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
