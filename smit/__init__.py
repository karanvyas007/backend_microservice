from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY'] = "147852369147852"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://remoteuser:root@192.168.1.103/campfood_webapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from smit import routes