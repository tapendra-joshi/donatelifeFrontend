import requests
from config import Config

def signup_user(data):

    headers = {"Content-Type": "application/json"}
    data = data
    url = Config.BACKEND_HOST+Config.SIGN_UP_ENDPOINT    
    response = requests.post(url,json=data,headers=headers)
    print(response)
    return response.json()