from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed

# Create the Flask-Bcrypt's instance
bcrypt = Bcrypt()

# Create the Flask-Login's instance
login_manager = LoginManager()

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(user_id):
    """ Load the user's info. """

    from app.models import User
    return User.query.filter_by(id=user_id).first()

# Create the Flask-Principal's instance
principals = Principal()

# Init the role permission iva RoleNeed(Need)
admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))
