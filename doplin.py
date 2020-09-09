
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json

n=0


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



url_base='https://lima.locanto.com.pe/Mujer-busca-hombre/20702/'

for x in range(20):

	url= url_base+str(x)

	print url

	r = requests.get(url, headers=headers)

	data = r.text

	soup = BeautifulSoup(data)


	for link in soup.find_all('a', class_='bp_ad__link'):

		_url = link.get('href')

		

		x = requests.get(_url, headers=headers)

		datax = x.text

		soupx = BeautifulSoup(datax)



		imagenes=[]

		for i in soupx.find_all('img', class_='browse_image_cropped'):

			imagen = i.get('data-src')

			imagenes.append(imagen)

		textHeader=''
		textDesc=''

		for i in soupx.find_all('span', class_='textHeader'):

			textHeader= i.text


		for i in soupx.find_all('span', class_='textDesc'):

			textDesc= i.text

		cont_anuncio=textHeader+' '+textDesc


		contenido = json.dumps({'wsp':'','edad':'','ciudad':'','anuncio':cont_anuncio,'imagenes':imagenes})
				
		try :

			cc = requests.post('http://aniavestidos.com:5000/guardalocanto', data = {'url':_url,'contenido':contenido})

		except:

			print 'Hay un error =('









