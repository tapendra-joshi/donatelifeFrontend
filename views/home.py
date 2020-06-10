
from flask import render_template,Blueprint,session,redirect,url_for,request
from services.get_all_blood_banks import get_all_blood_banks

blueprint = Blueprint("home",__name__,)

@blueprint.route('/',methods=["GET"])
@blueprint.route('/blood_banks/<page>',methods=["GET"])
def index(page=1):
    if session.get('logged_in',None):
        
        print("I am rendering")
        data_obj = get_all_blood_banks(page=page)["data"]
        data_obj_values = data_obj["blood_bank_data"].values()
        page_metadata = data_obj["page_metadata"]
        print(page_metadata)
        return render_template('index.html',title="Donate-Life",data_obj = data_obj_values,page_metadata=page_metadata)
    return redirect(url_for('login.login'))