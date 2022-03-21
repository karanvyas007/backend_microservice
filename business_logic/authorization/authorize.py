from flask_jwt_extended import create_access_token
import jwt
from business_logic import app
from flask_jwt import jwt_required
import datetime
from functools import wraps
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


class Autorization():
    """

    """

    def generate_token(self, username):
        """

        :param username:
        :param password:
        :return:
        """
        try:
            if username:
                # access_token = create_access_token(identity=username)
                access_token = jwt.encode(
                    {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
                    app.config['SECRET_KEY'])
                return access_token
        except Exception as e:
            print("token is not generated properly", str(e))
        return None
