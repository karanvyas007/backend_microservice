from smit import app
from flask import render_template,request
import socket
from flask import jsonify
from smit.models import Items


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
    return jsonify( HOSTNAME=hostname,HOSTIP=hostip)



@app.route('/test_t',methods=['GET','POST'])
def test_t():
    from smit.models import Items
    data = request.get_json()
    print(data)
    return jsonify(show_data=data)