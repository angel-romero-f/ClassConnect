from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Role
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/user_login')
def login():
    return render_template('login.html')

@auth.route('/user_login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # Gathers info from the form
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    role_name = request.form.get('role')
    #role = request.form.get('role')  # Get the selected role from the form

    # Check if the email already exists in the database
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        flash(f"Role '{role_name}' does not exist.")
        return redirect(url_for('auth.signup'))
    # Hash the password
    hashed_password = generate_password_hash(password, "pbkdf2")
    new_user = User(email=email, name=name, password=hashed_password, fs_uniquifier=email,active=True, roles = role)
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))