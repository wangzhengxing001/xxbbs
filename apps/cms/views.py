from flask import Blueprint, request, render_template, url_for, session, redirect, views, g
from .forms import LoginForm, ChangePwdForm
from .models import CMSUser
from .decorators import login_required
from config import CMS_USER_ID
from exts import db, mail
from utils import restfuls
from flask_mail import Message
bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route("/")
@login_required
def index():
    return render_template("cms/index.html")


# 测试邮箱
@bp.route("/sendmail/")
def send_mail():
    msg = Message("更改邮箱验证", recipients=["12345465489799999997979s@qq.com"], body="测试邮件!")
    result = mail.send(msg)
    return "abc"


# 注销功能
@bp.route("/loginout/", endpoint="loginout")
@login_required
def login_out():
    # session[CMS_USER_ID] = None
    del session[CMS_USER_ID]
    return redirect(url_for("cms.login"))


# 登陆跳转及验证
class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template("cms/login.html", message=message)

    def post(self):
        loginForm = LoginForm(request.form)
        if loginForm.validate():
            email = loginForm.email.data
            password = loginForm.password.data
            remember = loginForm.remember.data
            user = CMSUser.query.filter_by(email=email).first()  # type:CMSUser
            if user and user.check_passowrd(password):
                session[CMS_USER_ID] = user.id
                if remember:
                    # 设置session的过期时间为1个月
                    session.permanent = True
                return redirect(url_for("cms.index"))
            else:
                return self.get(message="账号密码不匹配!")
        else:
            error = loginForm.get_errors()
            return self.get(message=error)


# 修改密码跳转与验证
class ChangepwdView(views.MethodView):
    def get(self):
        return render_template("cms/change_pwd.html")

    def post(self):
        changeForm = ChangePwdForm(request.form)
        if changeForm.validate():
            cms_user = g.cms_user # type:CMSUser
            if cms_user.check_passowrd(changeForm.old_password.data):
                cms_user.password = changeForm.new_password.data
                db.session.commit()
                return restfuls.success(message="修改成功!")
            else:
                return restfuls.param_error(message="原始密码错误!")
        else:
            return restfuls.param_error(message=changeForm.get_errors())


# 修改邮箱跳转与验证
class ChangeMailView(views.MethodView):
    def get(self):
        return render_template("cms/change_mail.html")

    def post(self):
        pass


bp.add_url_rule("/changemail/", view_func=ChangeMailView.as_view("changemail"))
bp.add_url_rule("/login/", view_func=LoginView.as_view("login"))
bp.add_url_rule("/changepwd/", view_func=ChangepwdView.as_view("changepwd"))