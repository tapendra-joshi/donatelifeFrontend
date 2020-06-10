from flask import render_template,Blueprint,request,redirect,url_for,flash,session
from services.logout_service import logout_user

blueprint = Blueprint("logout",__name__)

@blueprint.route("/logout",methods=["GET"])
def logout():
    
    resp = logout_user()
    if resp.status_code == 200:
        session.pop("email",None)
        session.pop("user_name",None)
        session["logged_in"] = False
        return redirect(url_for('login.login'))
    return redirect(url_for('home.index'))
    