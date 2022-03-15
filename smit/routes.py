from smit import app
from flask import render_template,request
import socket
from flask import jsonify


@app.route('/main')
def main_page():
    return jsonify(status="active",message="you are in index page")

@app.route('/fetch')
def Fetch():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return  str(hostname), str(hostip)

@app.route('/health',methods=['GET','POST'])
def health():
    hostname,hostip=Fetch()
    return render_template("main.html", HOSTNAME=hostname,HOSTIP=hostip)


@app.route('/test_t',methods=['GET','POST'])
def test_t():
    return "ok"