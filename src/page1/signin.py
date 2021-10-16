import requests
from bs4 import BeautifulSoup
import functions
import time
# SIGN IN
def signin(sesion):
    register = 'https://w3.gamehost.cl/register.php'
    capcha = 'https://w3.gamehost.cl/includes/verifyimage.php'

    r = sesion.get(register)
    c = sesion.get(capcha)
    token = functions.token(r.content)
    token = functions.replace(",'", token)
    codigo = functions.catpcha(r.content)
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

    r = sesion.post(register, data=payload)
    print(r.text)
        