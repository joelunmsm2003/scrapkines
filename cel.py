#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests

import json


html = "<div id='anuncio_telefono'><a class='boton_telefono anuncio_telefono' data-posicion='top' href='tel:947697406'></a><table cellpadding='0' cellspacing='0'><tr><td class='boton_icono'><i class='material-icons'>phone</i></td><td class='boton_texto'>947 697 406</td></tr></table></div>"

soup = BeautifulSoup(html)



for wsp in soup.find_all('td', class_='boton_texto'):

	print wsp.get_text()
