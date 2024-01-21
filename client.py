import requests, json

ep = "http://127.0.0.1:5000/showdata"
re = requests.get(ep)
di = re.json()
print(di)
