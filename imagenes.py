from bs4 import BeautifulSoup
import json
import requests
import re
import sys
import linecache
import os
import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

formato=" {:<5} {:<10} {:<10} {:<10}"


r  = requests.get("https://kinesiologasenlima.com")
data = r.text
soup = BeautifulSoup(data)

urls=[]

for link in soup.find_all('a'):

	urls.append(link.get('href'))


urls= list(dict.fromkeys(urls))



def extrae(url):

	print('URL ',HEADER+url+ENDC)
	try:
		r  = requests.get(url)
		status_code=r.status_code
	except:
		status_code=400

	print(HEADER+str(status_code)+ENDC)

	if int(status_code)==200:

		data = r.text

		soup = BeautifulSoup(data)

		for link in soup.find_all('a', class_='item-link'):

			url = link.get('href')

			x = requests.get(url)

			datax = x.text

			soupx = BeautifulSoup(datax)

			for a in soupx.find_all('a', class_='btn-telefono'):

				fono=a.text.replace(' ','').replace('Llamar','').replace('-','')

			for a in soupx.find_all('div', class_='anuncio-ficha'):

				j=0
				for im in a.find_all('span'):

					if j==0:
						ciudad=im.text.replace('-','').replace('\n', ' ').replace('\r', '').replace(',', '')
					if j==1:
						edad=im.text.split('|')[1].replace('-','').replace('\n', ' ').replace('\r', '').replace(',', '').replace('años', '')
						try:
							precio=im.text.split('|')[2].replace('-','').replace('\n', ' ').replace('\r', '').replace(',', '')
						except:
							precio='-'
					j=j+1

			for a in soupx.find_all('div', class_='anuncio-descripcion'):

				cont_anuncio=a.text.replace(' ','').replace('-','').replace('\n', ' ').replace('\r', '').replace(',', '')

			imagenes=[]

			for a in soupx.find_all('div', class_='anuncio-fotos'):
			
				for im in a.find_all('img'):

					imagenes.append(im.get('src'))

					os.system('curl -O '+im.get('src'))
					os.system('mv *.jpg imagenes')


			contenido = json.dumps({'wsp':fono,'edad':edad,'ciudad':ciudad,'anuncio':cont_anuncio,'imagenes':imagenes,'fono':fono})
			
			'''	
			dat= requests.get('https://aniavestidos.com:5000/verificatelefono/'+str(fono))

			print(formato.format(edad,ciudad,fono,dat.text))

			if dat.text!='"no"':

				cc = requests.post('https://aniavestidos.com:5000/guardaskinelima', data = {'url':url,'contenido':contenido})

			'''


for u in urls:

	extrae(u)


	