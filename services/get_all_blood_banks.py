import requests

def get_all_blood_banks(page = 1):
    url = "https://donate-life.herokuapp.com/"
    endpoint = "blood_banks/all"
    payload = {"page":page}
    HEADERS = {"Content-Type": "application/json"}
    response = requests.request(
        "GET",url+endpoint,headers=HEADERS,params=payload)
    print(response)
    if response:
        return response.json()
    return None