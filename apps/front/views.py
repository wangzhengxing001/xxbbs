from flask import Blueprint

bp = Blueprint("front", __name__, url_prefix="/front")


@bp.route("/")
def index():
    return "front page"