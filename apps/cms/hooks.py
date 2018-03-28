from .views import bp
from config import CMS_USER_ID
from flask import session, g
from .models import CMSUser

@bp.before_request
def before_request():
    if CMS_USER_ID in session:
        user_id = session.get(CMS_USER_ID)
        cms_user = CMSUser.query.filter(CMSUser.id == user_id).first()
        if cms_user:
            g.cms_user = cms_user
        else:
            g.cms_user = None