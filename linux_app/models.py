from datetime import datetime
from linux_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def check_mac(mac_address) -> str:
    '''
    Returns a string data of the mac address is found, else, ""
    '''
    return Host.query.get(str(mac_address)) 

class User(db.Model, UserMixin):
    #__tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # Magic method
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"


class Host(db.Model):
    #__tablename__ = 'mac_queries'
    hardware = db.Column(db.String(20), primary_key=True)
    parent_name = db.Column(db.String(30), unique=False, nullable=True)
    parent_type = db.Column(db.String(30), unique=False, nullable=True)
    parent_port = db.Column(db.String(30), unique=False, nullable=True)
    fingerprint = db.Column(db.String(30), unique=False, nullable=True)
    address = db.Column(db.String(30), unique=False, nullable=True)

    def __repr__(self):
        return f"Host('{self.parent_name}', '{self.parent_port}', '{self.fingerprint}', '{self.address}', '{self.hardware}' )"
