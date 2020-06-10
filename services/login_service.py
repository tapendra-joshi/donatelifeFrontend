import requests
from config import Config

def login_user(data):
    headers = {"Content-Type": "application/json"}
    url = Config.BACKEND_HOST+Config.SIGN_IN_ENDPOINT
    response = requests.post(url,json=data,headers=headers)

    return response
