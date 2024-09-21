from .db import db
from .models import Role

def create_roles():
    # Check if roles already exist
    if not Role.query.filter_by(name='Student').first():
        student = Role(name='Student')
        db.session.add(student)

    if not Role.query.filter_by(name='Teacher').first():
        teacher = Role(name='Teacher')
        db.session.add(teacher)

    if not Role.query.filter_by(name='Parent').first():
        parent = Role(name='Parent')
        db.session.add(parent)

    db.session.commit()
    print("Roles created successfully!")