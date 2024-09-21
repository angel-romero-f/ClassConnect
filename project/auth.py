from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Student, Parent, Teacher
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
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

    if Parent.query.filter_by(id=user.id).first():
        return redirect(url_for('main.parent_dashboard'))
    elif Student.query.filter_by(id=user.id).first():
        return redirect(url_for('main.student_dashboard'))
    elif Teacher.query.filter_by(id=user.id).first():
        return redirect(url_for('main.teacher_dashboard'))
    else:
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
    role = request.form.get('role')  # Get the selected role from the form

    # Check if the email already exists in the database
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # Hash the password
    hashed_password = generate_password_hash(password, "pbkdf2")

    # Create the appropriate user based on their role
    if role == 'student':
        new_user = Student(email=email, name=name, password=hashed_password)
    elif role == 'parent':
        new_user = Parent(email=email, name=name, password=hashed_password)
    elif role == 'teacher':
        new_user = Teacher(email=email, name=name, password=hashed_password)
    else:
        flash('Invalid role selected. Please try again.')
        return redirect(url_for('auth.signup'))

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))