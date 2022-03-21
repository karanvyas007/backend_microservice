import json
import socket
from flask import jsonify,make_response
from flask import request
from business_logic import app
import jwt
from flask_jwt import jwt_required
import datetime
from functools import wraps
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token



@app.route('/main')
def main_page():
    return jsonify(status="active", message="you are in index page")


@app.route('/fetch')
def Fetch():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return str(hostname), str(hostip)


@app.route('/health', methods=['GET', 'POST'])
def health():
    hostname, hostip = Fetch()
    return jsonify(HOSTNAME=hostname, HOSTIP=hostip)


@app.route('/items', methods=['GET', 'POST'])
def items():
    from business_logic.models.models import Items,Registration
    data1 = Items.query.all()
    data_list = []
    for i in data1:
        temp = {"cat_id": i.cat_id, "item_id": i.item_id,
                "item_img": i.item_img, "item_name": i.item_name,
                "item_price": i.item_price}
        data_list.append(temp)
    print(data1)
    return json.dumps(data_list)


@app.route("/register", methods=['POST'])
def register():
    """
    :return:
    all the data
    """
    try:
        data = request.get_json()
        print(data)
        from business_logic import db
        from business_logic.models.models import Registration
        print(data.get('username'))
        register_data = Registration(fullname=data.get('fullname'), username=data.get('username')
                                     , email=data.get('email'), password=data.get('password'), ph_no=data.get('ph_no'))

        print(register_data.email)
        print(register_data.password)
        print(register_data.ph_no)
        print(register_data.fullname)
        db.session.add(register_data)
        db.session.commit()
        record=Registration.query.filter_by(username=register_data.email)
        # print(data['username']) #aa riete bi data get kari sakay
        responce = {"status": "True", "message": "data stored successfully",}
        return responce
    except:
        responce = {"status": "False", "message": "data do not stored successfully"}
        return responce


@app.route('/login', methods=['POST'])
def login():
    try:
        from business_logic.models import Registration
        if request.method == "POST":
            data = request.get_json()
            print(data)
            username = data.get('username')
            password = data.get('password')
            print(username)
            print(password)
            user = Registration.query.filter_by(username=username).first()
            if user:
                if password == user.password:
                    response = {"status":  True , "message": "Logged in sucessfully","flag": "1"}
                    return response
                else:
                    response = {"status": "False", "message": "please enter valid password","flag": "0"}
                    return response
            else:
                response = {"status": "False", "message": "Please enter valid input"}
                return response
    except:
        response = {"status": "404", "message": "enter valid input"}
        return response

@app.route('/auth',methods=['GET'])
def authentication():
    auth = request.authentication
    if auth and auth.password == 'admin@1234':
        token = jwt.encode(
            {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            app.config['SECRET_KEY'])
        # return jsonify({'token':token.decode('utf-8')})
        return jsonify({'token': token})
    else:
        return make_response('coul-d not verify', 401, {'Authentication': 'login required"'})

@app.route('/auth2', methods=['POST'])
def auth_fn():
    username = request.json.get("username")
    password = request.json.get("password")
    if username == "admin@gmail.com" or password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

