# -*- coding: UTF-8 -*-
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import db, User, Post, Comment, Tag, Role
import app.models
from app.config import DevConfig

# Create thr app instance via Factory Method
app = create_app(DevConfig)
# Init manager object via app object
manager = Manager(app)

# Init migrare object via app and db object
migrate = Migrate(app, db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server(host='0.0.0.0', port=8080))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Post=Post,
                Comment=Comment,
                Tag=Tag,
                Role=Role)


if __name__ == '__main__':
    manager.run()
