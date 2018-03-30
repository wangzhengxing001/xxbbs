from wtforms import Form
from wtforms.fields import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from apps.common.forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="邮箱格式错误!")])
    password = StringField(validators=[Length(6, 20, message="密码格式错误!")])
    remember = IntegerField()


class ChangePwdForm(BaseForm):
    old_password = StringField(validators=[Length(6, 20, message="原始密码格式不正确!")])
    new_password = StringField(validators=[Length(6, 20, message="新密码密码格式不正确!")])
    re_new_password = StringField(validators=[EqualTo("new_password", message="两次输入的密码不一致!")])
