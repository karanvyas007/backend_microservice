import json

from flask import jsonify
from flask import request

from business_logic import app
from business_logic import db
from business_logic.authorization.authorize import Autorization
from business_logic.models.cart import Cart
from business_logic.models.items import Items
from business_logic.models.registration import Registration


@app.route('/main')
def main_page():
    return jsonify(status="active", message="you are in index page")


@app.route('/items', methods=['GET', 'POST'])
def items():
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
            fullname
            username
            email
            password
            ph_no
            commit all the data into "Registration" table in database

    :return:
    the valid response in json formate and also
    return the token for token validation for login,
    """
    response = {"status": "False", "message": "Error occurred"}
    try:
        data = request.get_json()
        print(data)

        print(data.get('username'))

        register_data = Registration(
            fullname=data.get('fullname'),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            ph_no=data.get('ph_no')
        )

        # print(register_data.email)
        # print(register_data.password)
        # print(register_data.ph_no)
        # print(register_data.fullname)
        print(register_data)  # aaana ma tame je models ma f string ma lakhia a print thay

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
    return return_response


@app.route('/delete', methods=['DELETE'])
def delete():
    return_response = {"status": "True", "message": "Account Deleted"}
    try:
        data = request.get_json()
        print(data)
        del_user = Registration.query.filter_by(username=data).first()
        db.session.delete(del_user)
        db.session.commit()
    except Exception as e:
        print(e)
        return_response = {"message": "Error Occurred in Delete"}
    return return_response


@app.route('/fooditems', methods=['POST'])
def fooditems():
    re_response = {"status": "False", "message": "please enter valid order"}
    try:
        if request.method == "POST":
            data = request.get_json()
            order_data = Cart(
                order_detail=data.get('order_detail'),
                total_amount=data.get('total_amount')
            )
            print(order_data)
            db.session.add(order_data)
            db.session.commit()
            re_response = {"status": True, "message": "Your order has been confirmed..!!"}

    except Exception as E3:
        print(E3)
        re_response = {"message": "Exception occurred"}
    return re_response
