from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .db import db

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'put some secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    from .models import User

    db.init_app(app)
    with app.app_context():
        db.create_all()

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