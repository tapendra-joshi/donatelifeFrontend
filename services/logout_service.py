import requests
from config import Config

def logout_user():
    headers = {"Content-Type": "application/json"}
    url = Config.BACKEND_HOST+Config.SIGN_OUT_ENDPOINT
    response = requests.post(url,headers=headers)
    return response