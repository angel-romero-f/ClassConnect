from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .db import db
from .create_roles import create_roles
from flask_security import Security, SQLAlchemySessionUserDatastore

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'put some secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

    from .models import User, Role

    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_roles()

    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for main parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for non-auth parts of app
    from .nonauth import nonauth as nonauth_blueprint
    app.register_blueprint(nonauth_blueprint)

    return app
