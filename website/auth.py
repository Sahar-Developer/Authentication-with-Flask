from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
# this is going to save the password in a more secure way in which you can not inverse the password(by giving x you'll have y but by giving y you cannot have x
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth' , __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Sign up first!', category='error')

    return render_template("login.html", user=None)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4 :
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
