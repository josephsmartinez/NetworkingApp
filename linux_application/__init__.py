from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from models import User, Data, OtherData

# Auth tokens will need to be created
#from flask_jwt

app = Flask(__name__)

# Research this
app.config['SECRET_KEY'] = '6dfed37d10b6d7034c0ebbb2972bd97d'
app.config['MARIA_DB_URI'] = '127.0.0.1'
db = SQLAlchemy(app)

from linux_application import routes