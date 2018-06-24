# -*- coding: UTF-8 -*-
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app
import app.models

# Init manager object via app object
manager = Manager(main.app)

# Init migrare object via app and db object
migrate = Migrate(main.app, models.db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server(host='0.0.0.0', port=8080))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)


if __name__ == '__main__':
    manager.run()
