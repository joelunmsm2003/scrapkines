import requests
import json

data=requests.get('https://aniavestidos.com:5000/kinesphoto')

print(json.loads(data.text))

data=json.loads(data.text)

data= list(filter(lambda x: x['origen']=='Locanto', data))

data= list(filter(lambda x: x['favorito']==True, data))

data=list(map(lambda x: x['url'], data))

print data


for u in data:

	print u