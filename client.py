import requests, json

ep = "http://127.0.0.1:5000/showdata"
re = requests.get(ep)
di = re.json()
print(di)

'{ Lembrando que a saída em json é necessária para getar no client}'
