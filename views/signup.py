from flask import render_template,Blueprint,request,redirect,url_for,flash
from .home import index
from services.signup_service import signup_user

blueprint = Blueprint("signup",__name__)

@blueprint.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":

        email = request.form.get("email",None)
        password = request.form.get("password",None)
        c_password  =request.form.get("confirm_password",None)
        # print(email)
        # print(password)
        # print(c_password)
        if email and password and c_password:
            if password == c_password:
                data = {"email":email,"password":password}
                resp = signup_user(data)
                if resp["data"]:
                    return redirect(url_for('home.index'))
                flash(resp["message"])
                return render_template('signup.html',title='Sign Up')
            flash("password and confirm password didn't matched!!!!!!!!!!")
            return render_template('signup.html')
        flash("not all values provided!!!!!!!!!")
        return render_template('signup.html',title='Sign Up')
    
    return render_template('signup.html')