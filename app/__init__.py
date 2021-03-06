from flask import Flask, redirect, url_for

from app.models import db
from app.controllers import blog, main
from app.extensions import bcrypt, login_manager, principals
from flask_principal import identity_loaded, UserNeed, RoleNeed
from flask_login import current_user


def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    # Set the app config
    app.config.from_object(object_name)

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)

    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    # Init the Flask-Login via app object
    login_manager.init_app(app)

    # Init the Flask-Prinicpal via app object
    principals.init_app(app)

    @app.route('/')
    def index():
        # Redirect the Request_url '/' to '/blog/'
        return redirect(url_for('blog.home'))

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """Change the role via add the Need object into Role.

                   Need the access the app object.
                """

        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app

