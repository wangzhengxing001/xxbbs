from flask import session, url_for, redirect
from functools import wraps


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if "user_id" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("cms.login"))
    return inner
