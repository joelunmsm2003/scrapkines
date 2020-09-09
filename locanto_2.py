#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import requests
import re


n=0
for n in range(0,100):

	print 'NNNNNN:',n


	if n==0:

		r  = requests.get("https://lima.locanto.com.pe/Mujer-busca-hombre/20702/")

	else:

		r  = requests.get("https://lima.locanto.com.pe/Mujer-busca-hombre/20702/"+str(n))

	data = r.text

	soup = BeautifulSoup(data)

	
	for link in soup.find_all('a', class_='bp_ad__link'):
	    
		url = link.get('href')

		x = requests.get(url)

		datax = x.text



		soupx = BeautifulSoup(datax)

		


		print 'entre'

		for linkx in soupx.find_all('div', class_='user_content'):

			contenido = str(linkx)

			contenido = contenido.replace('<div class="user_content" id="js-user_content" itemprop="description">','').replace('<br>','').replace('<br/>','').replace('  ','').replace('<div>','').replace('</div>','')

			

			fono=contenido[3:15].replace(' ','').replace(',','').replace('%','').replace('.','')


			fono = re.sub('[^a-zA-Z0-9 \n\.]', '', fono)
			edad=''

			if 'trans' in contenido or 'busco a una chica' in contenido or 'TRAVESTI' in contenido:

				pass

			else:

				print 'contenido',contenido,

				length=len(contenido.split('años')[0])

				if len(contenido.split('años'))>1:
					edad=str(contenido.split('años')[0])[length-4:length-1]

				length=len(contenido.split(' 9')[0])

				if len(contenido.split(' 9'))>1:
					fono=str('9'+str(contenido.split(' 9')[1])[0:8]).replace(' ','')


				try:

					_contenido = json.dumps({'distrito':'','fono':fono,'anuncio':str(contenido),'imagenes':'','detalle':'','edad':edad,'precio':''})


					print fono
				

					dat= requests.get('https://aniavestidos.com:5000/verificatelefono/'+str(fono))

					print 'Verificando...',dat.text


					if dat.text!='"no"':

						print 'Entre..... =)'

						cc = requests.post('https://aniavestidos.com:5000/guardalocanto', data = {'url':url,'contenido':_contenido})

				except:

					print 'EROOOR'





			print '------'

		
		#cc = requests.post('http://mylookxpressapp.com:2000/guardaurl', data = {'url':url,'contenido':contenido})



