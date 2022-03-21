import datetime
import json
import socket

import jwt
from flask import jsonify, make_response
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from business_logic import app
from business_logic.authorization.authorize import Autorization
from business_logic.models.models import Registration


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
    from business_logic.models.models import Items
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
    response = {"status": "False", "message": "Error occurred"}
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
        # record = Registration.query.filter_by(username=register_data.email)
        # if record is not None:
        # print(data['username']) #aa riete bi data get kari sakay
        auth_obj = Autorization()
        token = auth_obj.generate_token(username=register_data.email)
        if token is not None:
            response = {"status": "True", "message": "data stored successfully", "token": token}
    except Exception as e1:
        response["message"] = "Exception occurred", str(e1)
    return response


@app.route('/login', methods=['POST'])
@jwt_required()
def login():
    """

    :return:
    """
    return_response = {"status": False, "message": "Error occurred"}
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            username = data.get('username')
            password = data.get('password')
            print(username)
            # print(password)
            user = Registration.query.filter_by(username=username).first()
            if user:
                if password == user.password:
                    return_response = {"status": True, "message": "Logged in successfully"}
                else:
                    return_response = {"status": False, "message": "Please enter a valid password"}
            else:
                return_response = {"status": "False", "message": "User does not exist."}
    except:
        return_response = {"status": False, "message": "Exception occurred."}

    return json.dumps(return_response)


# @app.route('/auth', methods=['GET'])
# def authentication():
#     auth = request.authentication
#     if auth and auth.password == 'admin@1234':
#         token = jwt.encode(
#             {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
#             app.config['SECRET_KEY'])
#         # return jsonify({'token':token.decode('utf-8')})
#         return jsonify({'token': token})
#     else:
#         return make_response('could not verify', 401, {'Authentication': 'login required"'})
#
#
# @app.route('/auth2', methods=['POST'])
# def auth_fn():
#     username = request.json.get("username")
#     password = request.json.get("password")
#     if username == "admin@gmail.com" or password == "admin":
#         access_token = create_access_token(identity=username)
#         return jsonify(access_token=access_token)
#     return jsonify({"msg": "Bad username or password"}), 401
