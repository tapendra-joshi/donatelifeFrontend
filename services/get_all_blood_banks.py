import requests

def get_all_blood_banks():
    url = "https://donate-life.herokuapp.com/"
    endpoint = "blood_banks/all?page=1"
    HEADERS = {"Content-Type": "application/json"}
    response = requests.request(
        "GET",url+endpoint,headers=HEADERS)
    print(response)
    if response:
        return response.json()
    return None