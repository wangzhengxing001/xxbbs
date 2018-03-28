from flask import Blueprint, request, render_template, url_for, session, redirect, views, g
from .forms import LoginForm
from .models import CMSUser
from .decorators import login_required
from config import CMS_USER_ID
bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route("/")
@login_required
def index():
    return render_template("cms/index.html")


# 注销功能
@bp.route("/loginout/", endpoint="loginout")
@login_required
def login_out():
    # session[CMS_USER_ID] = None
    del session[CMS_USER_ID]
    return redirect(url_for("cms.login"))


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
            error = loginForm.errors.popitem()[1][0]
            return self.get(message=error)


bp.add_url_rule("/login/", view_func=LoginView.as_view("login"))
