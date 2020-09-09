# -*- coding: utf-8 -*-

print "SSSSSSSSSSSSSSSSSSUCKING EVERYTHING IN SSSSSSSSSSSIGHT                  "
print "                                                                        "
print "              \                                                         "
print "               \                                                        "
print "                   /^\/^\                                               "
print "                 _|__|  O|                                              "
print "        \/     /~     \_/ \                                             "
print "         \____|__________/  \                                           "
print "                \_______      \                                         "
print "                        `\     \                 \                      "
print "                          |     |                  \                    "
print "                         /      /                    \                  "
print "                        /     /                       \\                "
print "                      /      /                         \ \              "
print "                     /     /                            \  \            "
print "                   /     /             _----_            \   \          "
print "                  /     /           _-~      ~-_         |   |          "
print "                 (      (        _-~    _--_    ~-_     _/   |          "
print "                  \      ~-____-~    _-~    ~-_    ~-_-~    /           "
print "                    ~-_           _-~          ~-_       _-~   - andy -"
print "                       ~--______-~                ~-___-~               "

             
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import requests

page = requests.get("https://facebook.com")


import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')


chrome_options.add_argument("--disable-infobars")
#chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

soup = BeautifulSoup(page.content, 'html.parser')

# http://dl.dropbox.com/u/49962071/blog/python/resource/bs_sample3.html

# soup = BeautifulSoup(html_content) # making soap

# for c in soup.find_all('.in-call-indicator-message'):

# print c




i=0


driver = webdriver.Chrome('/root/pegasus1/globo/chromedriver/chromedriver',chrome_options=chrome_options)

driver.get('https://www.facebook.com')

username = driver.find_element_by_id("email")

passw = driver.find_element_by_id("pass")

username.send_keys('912550323')

inicia = driver.find_element_by_id("u_0_b")

passw.send_keys('joelunmsm2003')

inicia.click()

time.sleep(5)



def trae(data):

	c=driver.find_element_by_xpath(data)

	print c.text

def click(data):

	c=driver.find_element_by_xpath(data)

	print c.click()

	time.sleep(5)

def ingresa(data,texto):

	c=driver.find_element_by_xpath(data)

	time.sleep(3)

	c.send_keys(texto)

'''
search='/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button'

click(search)'''

url='https://www.facebook.com/search/people/?q=Trabaja%20en%20Soy%20Una%20Princesa%20Y%20Las%20Princesas%20No%20Trabajan&epa=SERP_TAB'

driver.get(url)

#amigos='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]'

#amigos = driver.find_elements_by_id("BrowseResultsContainer")




driver.execute_script("window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight)") 

time.sleep(5)

b=1

a=1

c=1
while True:

	print c,b

	ami='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div['+str(c)+']/div/div/div['+str(b)+']/div'


		

	if a>=8:

		b=1
		
		a=1

		c=c+1

		driver.execute_script("window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight)") 

		time.sleep(3)
	

	a=a+1

	b=b+1

	time.sleep(.2)


	try:

		print 'Primer caso'

		imagen=driver.find_element_by_xpath(ami+'/div/div/div[1]/a/img')

		ref=driver.find_element_by_xpath(ami+'/div/div/div[1]/a')

		referencia= ref.get_attribute("href")

		foto= imagen.get_attribute("src")

		perfil=driver.find_element_by_xpath(ami)

		datos=perfil.text.splitlines()

		nombre=datos[0]

		trabajo=datos[2]


		for d in datos:

			if d.find("Vive en") != -1:
	
				vive=d

			
		print nombre,trabajo,vive,referencia

		url = 'https://aniavestidos.com:5000/facebook'

		myobj = {'nombre': nombre,'trabajo': trabajo,'vive':vive,'foto':foto,'referencia':referencia}

		x = requests.post(url, data = myobj)

		print x.text



	except:

		try:

			print 'Segundo caso'

			ami='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div['+str(c)+']/div/div['+str(b)+']/div'

			imagen=driver.find_element_by_xpath(ami+'/div/div/div[1]/a/img')

			ref=driver.find_element_by_xpath(ami+'/div/div/div[1]/a')

			referencia= ref.get_attribute("href")

			foto= imagen.get_attribute("src")

			perfil=driver.find_element_by_xpath(ami)

			datos= perfil.text.splitlines()

			nombre=datos[0]

			trabajo=datos[2]

			for d in datos:

				if d.find("Vive en") != -1:
		
					vive=d

			
			print nombre,trabajo,vive,referencia

			url = 'https://aniavestidos.com:5000/facebook'

			myobj = {'nombre': nombre,'trabajo': trabajo,'vive':vive,'foto':foto,'referencia':referencia}

			x = requests.post(url, data = myobj)

			print x.text


		except:

			print 'NO....'




'''

amigos = driver.find_elements_by_id("pagelet_loader_initial_browse_result")

for a in amigos:

	print a.text

	print '-----'


#ingresa(search,'carla')





perfil=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/ul/li/a/div')

click(perfil)

content = driver.find_element_by_partial_link_text('Información')

content.click()

time.sleep(3)

c = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[1]/ul/li[1]/div')

trabajo = c.text

c = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[1]/ul/li[2]/div')

print c.text

time.sleep(7)

c=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/ul/li[1]/div/div[2]/span/div[2]')

print c.text

c=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/ul/li[2]/div/div[2]/span/div[2]')

nacimiento='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/ul/li[2]/div/div[2]/span/div[2]'

formacion='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[1]/div/div/div/a[2]'

click(formacion)

empleo='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div/div[1]/ul/li[2]/div/div/div'

trae(empleo)

aptitud_profesional='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div/div[2]/ul/li/div/div[1]/div'

trae(aptitud_profesional)

universidad='//*[@id="u_u_4"]'

escuela='//*[@id="u_u_5"]'

lugar='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[1]/div/div/div/a[3]'

click(lugar)

ciudad_actual='//*[@id="current_city"]'

ciudad_origen='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div/div[1]/ul/li[2]/div/div[1]/div/div'

trae(ciudad_origen)

informacion_basica='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[1]/div/div/div/a[4]/span[1]'

click(informacion_basica)

sexo='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/div/ul/li[3]'

intereses='/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/div/ul/li[4]'

trae(sexo)




content = driver.find_element_by_partial_link_text('Franklin David')

print content.click()

time.sleep(3)

content = driver.find_element_by_partial_link_text('Información')

content.click()

time.sleep(3)

content = driver.find_element_by_class_name('clearfix')

print content.text

post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")

post_box.click()

post_box.send_keys("Testing using Name not ID.Selenium is easy.")

time.sleep(2)


driver.find_element_by_xpath("(//button[@value='1'])[5]").click();


print "Posted..."


#driver.close()



driver.get('https://www.globohq.com/users/sign_in');

username = driver.find_element_by_id("user_email")

password = driver.find_element_by_id("user_password")

usuario = "clara@activak.com"

username.click();



time.sleep(1)

username.send_keys(usuario)

password.click();

password.send_keys("Helloglob01234!")

driver.find_element_by_name("commit").click();

estado = driver.find_element_by_class_name('in-call-indicator-message')

print usuario,estado.text,datetime.datetime.today()

requests.get('http://localhost:8000/guarda/?usuario='+str(usuario)+'&estado='+str(estado.text))

driver.close()

pass

#password.send_keys("Pa55worD")

#driver.find_element_by_name("submit").click()

#driver.findElement(By.id("user_email")).sendKeys("555-55-5555"); 

# elem = driver.find_element_by_partial_link_text('Mostrar n')

# elem.click()

# elem = driver.find_element_by_class_name('number')

# number = elem.text

#driver.close()

'''
