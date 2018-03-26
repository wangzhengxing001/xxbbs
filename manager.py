from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from xxbbs import app
from exts import db
import apps.cms.models as cms_model
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.option("-u", "--username", dest="username")
@manager.option("-e", "--email", dest="email")
@manager.option("-p", "--password", dest="password")
def add_cms_user(username, password, email):
    user = cms_model.CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print("添加成功!")


if __name__ == '__main__':
    manager.run()
