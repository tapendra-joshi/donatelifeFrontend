from flask import render_template,Blueprint,request,redirect,url_for,flash,session
# from flask.ext.session import Session
from services.login_service import login_user
from .home import index

blueprint = Blueprint("login",__name__)

@blueprint.route("/login",methods =["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email',None)
        password = request.form.get('password',None)
        data = {"email":email,"password":password}
        if email and password:
            response = login_user(data)
            if response.status_code == 200:
                session["user_name"] = response.json()["data"]["first_name"]+" "+ response.json()["data"]["last_name"]
                session["email"] = email
                session["logged_in"] = True
                return redirect(url_for('home.index'))
            flash(response["message"])
            return render_template('login.html',title='Login')
    if session.get("logged_in",None):
        return redirect(url_for('home.index'))
    return render_template('login.html',title='Login')
