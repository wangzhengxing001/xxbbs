from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class CMSUser(db.Model):
    __tablename__ = "cms_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, password, email):
        self.password = password
        self.username = username
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_passowrd(self, raw_password):
        result = check_password_hash(self._password, raw_password)
        return result