import requests #importing the requests module 
import json #importing the json module


url = "https://yfapi.net/v6/finance/quote"

headers={
    "x-api-key":"SyKB6HKy718DtJGmxx5aw8CnxoC6vAqQ68pOXcj3"
}

params={"symbols":"AAPL,BTC-USD,EURUSD=X"}

def get_data():
    resp=requests.get(url,headers=headers,params=params)
    return resp.text

data=json.loads(get_data())

print(json.dumps(data,indent=4))



