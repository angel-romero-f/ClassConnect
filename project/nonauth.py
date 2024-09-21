from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .models import Class

nonauth = Blueprint('nonauth', __name__)

@nonauth.route('/home')
def home():
    return render_template('home.html')

@nonauth.route('/home', methods=['POST'])
@login_required
def create_classroom():
    # name of the class 
    # maybe days/times that they teach it 

    name = request.form.get('className')
    teacher_id = current_user.id
    teacher_name = current_user.name 
    classroom = Class(name = name, teacher_id = teacher_id, teacher=teacher_name)
    db.session.add(classroom)
    db.session.commit()
    return redirect(url_for('nonauth.home'))

@nonauth.route('/exit')
def exit_ticket():
    return render_template('exit.html')

@nonauth.route('/announcements')
def announcements():
    return render_template('announcements.html')

@nonauth.route('/chatroom')
def chatroom():
    return render_template('chatroom.html')
