#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json

n=0


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

edad=''

#url = ['https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/surco','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-isidro','https://www.photokinesiologas.com/kinesiologas/surquillo','https://www.photokinesiologas.com/kinesiologas/lince','https://www.photokinesiologas.com/kinesiologas/san-juan-de-miraflores','https://www.photokinesiologas.com/kinesiologas/cerca_-12.1061142,-77.0307285,3',u'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/18-21-años','https://photokinesiologas.com/kinesiologas/lima-metropolitana/san-martin-de-porres','https://photokinesiologas.com/kinesiologas/lima-metropolitana/venezolanas','https://photokinesiologas.com/kinesiologas/lima-metropolitana/','https://photokinesiologas.com/kinesiologas/','https://photokinesiologas.com/']

url=['https://pe.skokka.com/kinesiologas/?p=1','https://pe.skokka.com/kinesiologas/?p=3','https://pe.skokka.com/kinesiologas/?p=4']

for x in range(100):

	u='https://pe.skokka.com/kinesiologas/lima-metropolitana/?p='+str(x+1)

	print u


	try:

		r = requests.get(u, headers=headers)

		data = r.text

		soup = BeautifulSoup(data)

		print 'soup',soup.find_all('p')

	except:

		print 'error'

		data = ''

		soup = BeautifulSoup(data)




	for link in soup.find_all('p', class_='item-title'):

		print 'link',link

		soup =  BeautifulSoup(str(link))



		for a in soup.find_all('a'):

			url= a.get('href')

			print 'URL...',url


			x = requests.get(url, headers=headers)

			datax = x.text

		

			soupx = BeautifulSoup(datax)

			#print soupx

		
			imagenes=[]
			
			for i in soupx.find_all('div', class_='brick'):

				try:

				
					soupxi = BeautifulSoup(str(i))

					for ix in soupxi.find_all('v-lazy-image'):

						imagenes.append(ix.get('src'))


				

				except:

					pass


			for i in soupx.find_all('h6', class_='detailtag'):

				try:

				
					soupxi = BeautifulSoup(str(i))

					ciudad= soupxi.text.split('|')[3]
				

				except:

					pass

			
			for h in soupx.find_all('div', class_='mobilecontactbar'):

				try:

					soupxi = BeautifulSoup(str(h))

					for ix in soupxi.find_all('phone-button'):

						fono = ix.get('number')


				except:

					pass


			print 'TELEFONO EXTRAIDO......',fono

			detalle=[]

			for d in soupx.find_all('b'):

				try:

					for x in BeautifulSoup(str(d)).find_all('b')[0]:

						detalle.append(x)


					edad=detalle[0].split(' ')[0]
						


				except:

					pass


			for d in soupx.find_all('p',class_='text-justify'):

				try:

					cont_anuncio = d.text


				except:

					pass


			print edad


			contenido = json.dumps({'wsp':fono,'edad':edad,'ciudad':ciudad,'anuncio':'cont_anuncio','imagenes':imagenes,'fono':fono})
			
			try :

				dat= requests.get('https://aniavestidos.com:5000/verificatelefono/'+str(fono))

				print 'Verifica Tl',dat


				if dat.text!='"no"':

					print 'Entre..... =)'

					cc = requests.post('https://aniavestidos.com:5000/guardaskoka', data = {'url':url,'contenido':contenido})

			except:

				print 'Hay un error =('



			

