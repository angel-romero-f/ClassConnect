from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Parent(User):
    child_name = db.Column(db.String(100))

class Student(User):
    grade_level = db.Column(db.String(100))

class Teacher(User):
    subject = db.Column(db.String(100))