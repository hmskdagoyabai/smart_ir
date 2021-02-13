
from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/on')
def on():
    command = ['./send.sh', 'light:on']
    res = subprocess.run(command)
    if res:
        return "{'status':False}"
    else:
        return "{'status':True}"


@app.route('/off')
def off():
    command = ['./send.sh', 'light:off']
    res = subprocess.run(command)
    if res:
        return "{'status':False}"
    else:
        return "{'status':True}"


if __name__ == "__main__":
    app.run(debug=True)
