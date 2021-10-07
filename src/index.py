import requests
from bs4 import BeautifulSoup
import resolver
import cap
import re
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

# TOKEN
inicio = BeautifulSoup(r.content, 'html.parser')
token = inicio.find('script')
accessToken = re.search('var csrfToken = (?P<token>.*)', token.string)
print(token)
token = accessToken.group('token')
characters = ",'"

for x in range(len(characters)):
    token = token.replace(characters[x],"")

print(token)

# CAPCHAAAAA
with open('test.png', 'wb') as file:
    file.write(c.content)
cap.cambioColor('test.png')
time.sleep(1)
codigo = resolver.recognize('test2.png')
characters = ","

for x in range(len(characters)):
    codigo = codigo.replace(characters[x],"")

print(codigo)

time.sleep(1)
print(codigo)
credenciales = {
    'nombre': 'nadie',
    'lastname':'ghola',
    'email':'nadiees@gmail.com',
    'numero':'23546765',
    'direccion':'calle falsa',
    'ciudad':'chimbarongo',
    'state':'chile',
    'password':'hola1234'
}

payload = {
     'token':token,
     'register':"true",
     'firstname':credenciales['nombre'],
     'lastname':credenciales['lastname'],
     'email':credenciales['email'],
     'country-calling-code-phonenumber':"56",
     'phonenumber':credenciales['numero'],
     'companyname':"",
     'address1':credenciales['direccion'],
     'address2':"",
     'city':credenciales['ciudad'],
     'state':credenciales['state'], 
     'postcode':"",
     'country':"CL",
     'tax_id':"",
     'currency':"1",
     'password':credenciales['password'],
     'password2':credenciales['password'],
     'marketingoptin':"1",
     'code':codigo,
     'accepttos':"on"
 }

r = s.post(register, data=payload)
print(r.text)
      

print('-----------------------------------')


