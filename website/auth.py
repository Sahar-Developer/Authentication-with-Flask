from flask import Blueprint

auth = Blueprint('auth' , __name__)

@auth.route('/login')
def login():
    return "<p>LOGIN</p>"

@auth.route('/logout')
def logout():
    return "<p>LOGout</p>"

@auth.route('/signup')
def signup():
    return "<p>SignUp</p>"
