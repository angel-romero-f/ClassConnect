from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route("/")
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('nonauth.home'))
    else:
        return render_template('landing.html')

@main.route('/profile', methods=["GET"])
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/parent_dashboard', methods=["GET"])
@login_required
def parent_dashboard():
    return render_template('parent_dashboard.html', name=current_user.name)

@main.route('/student_dashboard', methods=["GET"])
@login_required
def student_dashboard():
    return render_template('student_dashboard.html', name=current_user.name)

@main.route('/teacher_dashboard', methods=["GET"])
@login_required
def teacher_dashboard():
    return render_template('teacher_dashboard.html', name=current_user.name)