from smit import app
from flask import render_template,request
import socket
from flask import jsonify
import json
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
    data1=Items.query.all()
    data_list = []
    for i in data1:
        temp = {"cat_id":i.cat_id,"item_id":i.item_id,
                "item_img":i.item_img,"item_name":i.item_name,
                "item_price":i.item_price}
        data_list.append(temp)
    print(data1)
    return json.dumps(data_list)