from flask import Flask, render_template
from exts import db, mail
import config
from apps.cms.views import bp as cms_bp
from apps.common.views import bp as common_bp
from apps.front.views import bp as front_bp
from flask_wtf import CSRFProtect

app = Flask(__name__)
# 开启CSRF保护
CSRFProtect(app)
app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)


@app.route('/')
def hello_world():
    return render_template("abc.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
