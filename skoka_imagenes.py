#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import requests

import json

n=0


url = ['https://www.photokinesiologas.com/kinesiologas/san-juan-de-miraflores','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/villa-maria-del-triunfo','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/surco','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-isidro','https://www.photokinesiologas.com/kinesiologas/surquillo','https://www.photokinesiologas.com/kinesiologas/lince','https://www.photokinesiologas.com/kinesiologas/cerca_-12.1061142,-77.0307285,3',u'https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/18-21-años','https://photokinesiologas.com/kinesiologas/lima-metropolitana/san-martin-de-porres','https://photokinesiologas.com/kinesiologas/lima-metropolitana/venezolanas','https://photokinesiologas.com/kinesiologas/lima-metropolitana/','https://photokinesiologas.com/kinesiologas/','https://photokinesiologas.com/','https://www.photokinesiologas.com/kinesiologas/lima-metropolitana/san-miguel']


for u in url:

	print('Quueee')


	r  = requests.get(u)

	data = r.text



	soup = BeautifulSoup(data)




	for link in soup.find_all('a', class_='link_ficha'):

		print('href...',link.get('href'))

	

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

				print(precio)

			except:

				pass


		_telefono=[]

		telefono = ''





		imagenes = []

		for sobremi in soupx.find("div", {"class": "contenedor"}):

			try:

				imagen= sobremi.get('src')

				imagenes.append(imagen)

			except:

				pass

		for i in imagenes:

			os.system('curl -O '+i)
			os.system('mv *.jpg imagenes')


		

