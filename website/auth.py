from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
# this is going to save the password in a more secure way in which you can not inverse the password(by giving x you'll have y but by giving y you cannot have x
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth' , __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    return render_template("login.html", user=None)

@auth.route('/logout', methods= ['GET', "POST"])
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4 :
            flash('Email must be greater than 3 characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 characters. ', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=None)

@auth.route('/home')
def home():
    return render_template("home.html", user=None)
