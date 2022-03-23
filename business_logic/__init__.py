from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = "147852369147852"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://remoteuser:root@192.168.1.103/campfood_webapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
from business_logic import routes
