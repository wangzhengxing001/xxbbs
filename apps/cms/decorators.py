from flask import session, url_for, redirect
from functools import wraps
from config import CMS_USER_ID


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if CMS_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("cms.login"))
    return inner
