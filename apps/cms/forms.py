from wtforms import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo


class LoginForm(Form):
    email = StringField(validators=[Email(message="邮箱格式错误!")])
    password = StringField(validators=[Length(6, 20, message="密码格式错误!")])
    remember = IntegerField()


class ChangePwdForm(Form):
    old_password = StringField(validators=[Length(6, 20, message="密码格式不正确!")])
    new_password = StringField(validators=[Length(6, 20, message="密码格式不正确!")])
    re_new_password = StringField(validators=[Length(6, 20, message="密码格式不正确!"), EqualTo("new_password", message="两次输入密码不一致!")])
