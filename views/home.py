
from flask import render_template,Blueprint,session,redirect,url_for
from services.get_all_blood_banks import get_all_blood_banks

blueprint = Blueprint("home",__name__)

@blueprint.route('/',methods=["GET"])
@blueprint.route('/home',methods=["GET"])
def index():
    if session.get('logged_in',None):
        print("I am rendering")
        data_obj = get_all_blood_banks()["data"]["blood_bank_data"].values()
        page_metadata = get_all_blood_banks()["data"]["page_metadata"]
        return render_template('index.html',title="Donate-Life",data_obj = data_obj)
    return redirect(url_for('login.login'))