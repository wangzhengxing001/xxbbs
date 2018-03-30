USERNAME = "root"
PASSWORD = "admin"
DBHOST = "localhost"
PORT = "3306"
DATABASE = "xxbbs"
URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, DBHOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATE_AUTO_RELOAD = True
DEBUG = True
import os
SECRET_KEY = os.urandom(24)

CMS_USER_ID = "cms_user_id"

MAIL_SERVER = "smtp.163.com"
MAIL_PORT = 994
# MAIL_USE_TLS = True
MAIL_USE_SSL = True
# MAIL_DEBUG = 默认app.debug
MAIL_USERNAME = "xxbbsAdministrator@163.com"
MAIL_PASSWORD = "961215xx"
MAIL_DEFAULT_SENDER = "xxbbsAdministrator@163.com" # ：发送者