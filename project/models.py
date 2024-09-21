from . import db
from flask_login import UserMixin
from flask_security import RoleMixin
from datetime import datetime

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(UserMixin, db.Model):
    #general user table with email, password, name, and user role
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    roles = db.relationship('Role', secondary=roles_users, backref='roled')
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

class Class(db.Model):
    #model representing a class with the name of the class, announcements, teacher, and students associated with the class
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    teacher_id = db.Column(db.Integer)
    teacher = db.Column(db.String(100))
    #establishes relationships between classes and other models

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

# class Enrollment(db.Model):
#     #model with student, class their enrolled in, and their corresponding ids
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
#     class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), primary_key=True)
#     student = db.relationship('Student', back_populates='enrollments')
#     class_ = db.relationship('Class', back_populates='enrollments')

# class Announcement(db.Model):
#     #model with announcement title, content of announcement, class it's for, time created, and corresponding class id
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200))
#     content = db.Column(db.Text)
#     class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
#     class_ = db.relationship('Class', back_populates='announcements')
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)