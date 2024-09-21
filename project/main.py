from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route("/")
def landing():
    return render_template('landing.html')

@main.route('/profile', methods=["GET"])
def profile():
    return render_template('profile.html')

