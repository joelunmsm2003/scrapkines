#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json

n=0


url = ['https://www.photokinesiologas.com/kinesiologas/san-juan-de-miraflores','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/villa-maria-del-triunfo','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/surco','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-isidro','https://www.photokinesiologas.com/kinesiologas/surquillo','https://www.photokinesiologas.com/kinesiologas/lince','https://www.photokinesiologas.com/kinesiologas/cerca_-12.1061142,-77.0307285,3',u'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/18-21-años','https://photokinesiologas.com/kinesiologas/lima-metropolitana/san-martin-de-porres','https://photokinesiologas.com/kinesiologas/lima-metropolitana/venezolanas','https://photokinesiologas.com/kinesiologas/lima-metropolitana/','https://photokinesiologas.com/kinesiologas/','https://photokinesiologas.com/','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-miguel']


for u in url:

	print 'Quueee'


	r  = requests.get(u)

	data = r.text



	soup = BeautifulSoup(data)




	for link in soup.find_all('a', class_='link_ficha'):

		print 'href...',link.get('href')

	

		url = 'https://photokinesiologas.com'+link.get('href')



		x = requests.get(url)

		datax = x.text

		soupx = BeautifulSoup(datax)


		

		edad=''
		for anuncio in soupx.find_all("span", {"id": "anuncio_edad"}):

			try:
				
				edad = anuncio.get_text().replace('|','').replace(u'años','')

			except:

				pass


		precio=''
		for data in soupx.find_all('div', {"id": "anuncio_disponibilidad"}):

			try:
				
				precio = data.get_text()

				print precio

			except:

				pass


		_telefono=[]

		telefono = ''


		# 	try:

		# 		telefono =  wsp.get('data-telefono')

		# 		_telefono.append(telefono)

		# 		telefono=_telefono[0]

		# 	except:

		# 		for wsp in soupx.find_all('td', class_='boton_texto'):

		# 			try:

		# 				print wsp

		# 				telefono = wsp.get_text()

		# 			except:

		# 				pass

		for wsp in soupx.find_all('td', class_='boton_texto'):

			if wsp.get_text()!='WhatsApp':

				telefono = wsp.get_text().replace(' ','')


				print 'WSP.........',telefono


		for wsp in soupx.find_all('span', class_='boton_telefono whatsapp'):

			telefono=wsp.get('data-telefono')

			print 'TELEFONO 2........',telefono


		#for fono in soupx.find("div", {"id": "anuncio_telefono"}):

		#	try:

		#		telefono =  fono.get_text()
		#		print 'TELEFONO 3........',telefono

		#	except:

		#		pass


			


		total_cont_anuncio =[]

		'''

		for anuncio in soupx.find("div", {"id": "anuncio_texto"}):

			try:

				cont_anuncio =  anuncio.get_text()

				
				total_cont_anuncio.append(cont_anuncio)

			except:

				pass

		'''

		for anuncio in soupx.find_all("span"):



			if u'años' in anuncio.get_text():

				edad = anuncio.get_text().split(' ')[0]

			if 'S/.' in anuncio.get_text():

				precio = anuncio.get_text()

			if len(anuncio.get_text())==11:

				telefono = anuncio.get_text().replace(' ','')



		for anuncio in soupx.find_all("span",{"itemprop":"name"}):

			distrito= anuncio.get_text()









		imagenes = []

		for sobremi in soupx.find("div", {"class": "contenedor"}):

			try:

				imagen= sobremi.get('src')

				imagenes.append(imagen)

			except:

				pass

		listdetalle=[]

		for detalle in soupx.find_all("a", {"class": "anuncio_categoria categoria_sel_off"}):

			try:

				detalle= detalle.get_text()

				listdetalle.append(detalle)

			except:

				pass




		contenido = json.dumps({'distrito':distrito,'fono':telefono,'anuncio':total_cont_anuncio,'imagenes':imagenes,'detalle':listdetalle,'edad':edad,'precio':precio})


		print contenido
		try:

			dat= requests.get('https://aniavestidos.com:5000/verificatelefono/'+str(telefono))

			print 'Verificando...',dat.text


			if dat.text!='"no"':

				print 'Entre..... =)'

				cc = requests.post('https://aniavestidos.com:5000/photoguardaurlphoto', data = {'url':url,'contenido':contenido})

		except:

			print 'EROOOR'

		#else:

		#	print 'Actualizando..'

		#	cc = requests.post('http://aniavestidos.com:5000/photoguardaurlactualiza', data = {'url':url,'contenido':contenido})


		

