
import json
import argparse
from flask import Flask, jsonify, redirect, render_template
import subprocess
import requests
app = Flask(__name__)

json_path = "./config/val/val.json"


@app.route('/')
def hello():
    names = get_names()
    # return '<a href="/on_button">on</a><br><a href="/off_button">off</a><br><a href="/on" onclick="return false;">on</a>'
    return render_template('index.html', names=names)


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


@app.route("/names")
def names():
    names = get_names()
    ret = []
    for name in names:
        ret.append({'name': name})
    return jsonify(ret)


def send_ir(name):
    command = ['python', 'irrp.py', '-p', '-g27',
               '-f', json_path, name]
    res = subprocess.call(command)
    return res


def get_names():
    with open(json_path, "r") as f:
        records = json.load(f)
    keys = list(records.keys())
    keys.reverse()
    return keys


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
