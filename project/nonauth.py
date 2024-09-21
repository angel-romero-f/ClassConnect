from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Student, Parent, Teacher
from . import db

nonauth = Blueprint('nonauth', __name__)

@nonauth.route('/home')
def home():
    return render_template('home.html')

@nonauth.route('/exit')
def exit_ticket():
    return render_template('exit.html')

@nonauth.route('/announcements')
def announcements():
    return render_template('announcements.html')

@nonauth.route('/chatroom')
def chatroom():
    return render_template('chatroom.html')
