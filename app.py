from flask import Flask
from flask_session import Session
from config import Config
from views.home import blueprint as home_blueprint
from views.signup import blueprint as signup_blueprint
from views.login import blueprint as login_blueprint
from views.logout import blueprint as logout_blueprint

application = app = Flask(__name__)



def create_app(config_class=Config):
    configure_config(app)
    configure_blueprint(app)

def configure_config(app,config_class=Config):

    app.config.from_object(config_class)
    
    return None

def configure_blueprint(app):
    print("I am registering blueprints")
    app.register_blueprint(home_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    return None

def configure_session(app):
    sess = Session()
    sess.init_app(app)
    return None

create_app()
if __name__=='__main__':
    app.run()