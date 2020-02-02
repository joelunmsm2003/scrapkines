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

	print 'data',data

	soup = BeautifulSoup(data)



	for link in soup.find_all('a', class_='link_anuncio'):

		print 'href...',link.get('href')

	

		url = 'https://photokinesiologas.com'+link.get('href')

		try:

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

			for wsp in soupx.find_all('span', class_='boton_telefono whatsapp'):

				try:

					telefono =  wsp.get('data-telefono')

					_telefono.append(telefono)

					telefono=_telefono[0]

				except:

					for wsp in soupx.find_all('td', class_='boton_texto'):

						try:

							print wsp

							telefono = wsp.get_text()

						except:

							pass


			total_cont_anuncio =[]

			for anuncio in soupx.find("div", {"id": "anuncio_texto"}):

				try:

					cont_anuncio =  anuncio.get_text()

					
					total_cont_anuncio.append(cont_anuncio)

				except:

					pass



			for anuncio in soupx.find_all("span", {"id": "anuncio_poblacion"}):


				distrito =  anuncio.get_text()





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

			print 'telefono.....',telefono

			try:

				dat= requests.get('http://aniavestidos.com:5000/verificatelefono/'+str(telefono))

				print 'Verificando...',dat.text


				if dat.text!='"no"':

					print 'Entre..... =)'

					cc = requests.post('http://aniavestidos.com:5000/photoguardaurlphoto', data = {'url':url,'contenido':contenido})

			except:

				pass

		except:

			print 'ERROR PHOTOKINES URL'

			pass

		#else:

		#	print 'Actualizando..'

		#	cc = requests.post('http://aniavestidos.com:5000/photoguardaurlactualiza', data = {'url':url,'contenido':contenido})


		

