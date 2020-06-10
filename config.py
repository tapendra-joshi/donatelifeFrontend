from dotenv import load_dotenv
import os
import redis


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
load_dotenv(os.path.join(basedir, '.env'),verbose=False)


class Config:
    DEBUG = True
    SIGN_UP_ENDPOINT = os.environ.get("SIGN_UP_ENDPOINT",None)
    SIGN_IN_ENDPOINT = os.environ.get("SIGN_IN_ENDPOINT",None)
    SIGN_OUT_ENDPOINT = os.environ.get("SIGN_OUT_ENDPOINT",None)
    BACKEND_HOST = os.environ.get("BACKEND_HOST",None)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_REDIS = redis.from_url(os.environ.get("SESSION_REDIS"))
    SESSION_TYPE = os.environ.get('SESSION_TYPE','redis')
