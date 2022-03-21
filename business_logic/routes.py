import json
import socket

from flask import jsonify
from flask import request

from business_logic import app
from business_logic import db
from business_logic.authorization.authorize import Autorization


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
# @jwt_required()
def login():
    """

    :return:
    """
    from business_logic.models.models import Registration
    return_response = {"status": False, "message": "Error occurred"}
    try:
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
                    return_response = {"status": True, "message": "Logged in sucessfully", "flag": "1"}
                    return return_response
                else:
                    return_response = {"status": "False", "message": "please enter valid password", "flag": "0"}
                    return return_response
            else:
                return_response = {"status": "False", "message": "Please enter valid input"}
                return return_response
    except Exception as e1:
        return_response["message"] = "Exception occurred", str(e1)
    return_response


@app.route('/delete/<int:Sno>')
def delete(Sno):
    return_response = {"status": "True", "message": "Account Deleted"}
    try:
        from business_logic.models.models import Registration
        del_user = Registration.query.filter_by(Sno=Sno).first()
        db.session.delete(del_user)
        db.session.commit()
    except Exception as d1:
        return_response = {"message": "Error Occured in Delete"}
    return return_response

