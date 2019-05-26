from app import create_app, db
from flask_script import Manager
from app.models import User, Comments
from flask_migrate import Migrate, MigrateCommand


app = create_app('test')

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comments=Comments)


if __name__ == '__main__':
    manager.run()
