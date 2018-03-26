from wtforms import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    email = StringField(validators=[Email(message="邮箱格式错误!")])
    password = StringField(validators=[Length(6, 20, message="密码格式错误!")])
    remember = IntegerField()
