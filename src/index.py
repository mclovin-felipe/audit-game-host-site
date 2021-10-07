import requests
from bs4 import BeautifulSoup
import resolver
import cap
import time
# ---------------------------------------------------------------------------------------------
# # LOG IN

s = requests.Session()

# payload = {'username': 'nada122@gmail.com', 'password': 'javi2602'}
# url = 'https://w3.gamehost.cl/dologin.php'

# r = s.post(url, data=payload)
# # r =requests.post(url, data=payload)
# inicio = BeautifulSoup(r.content, 'html.parser')

# entrada = inicio.find(menuitemname="Client Details")
# if entrada == None:
#     print("Pass incorrecta")
# else:
#     print("dentrop")


# ---------------------------------------------------------------------------------------------




# SIGN IN

register = 'https://w3.gamehost.cl/register.php'
capcha = 'https://w3.gamehost.cl/includes/verifyimage.php'

r = s.get(register)
c = s.get(capcha)
print('-----------------------------------')


with open('test.png', 'wb') as file:
    file.write(c.content)
cap.cambioColor('test.png')

resolver.recognize('test2.png')