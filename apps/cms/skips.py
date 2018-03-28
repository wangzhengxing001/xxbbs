from .views import bp, login_required
from flask import render_template


# 首页
@bp.route("/mainpage/", endpoint="mainpage")
@login_required
def mainpage():
    return render_template("cms/main.html")


# 个人中心页面
@bp.route("/profile/", endpoint="profile")
@login_required
def profile():
    return render_template("cms/profile.html")
