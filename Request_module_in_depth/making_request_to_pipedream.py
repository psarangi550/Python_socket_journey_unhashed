import requests

url="http://api.open-notify.org/iss-now.json/d_dls4d6nQ"

headers={

}
try:
    resp=requests.get(url)
    print(resp.text)
except requests.exceptions.SSLError:
    print("Not happening")
