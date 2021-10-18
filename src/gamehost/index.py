from PIL.Image import new
import requests
from bs4 import BeautifulSoup
import resolver
import cap
import re
import time
# ---------------------------------------------------------------------------------------------
# # LOG IN

s = requests.Session()
def inicio(email, password):
    payload = {'username': email, 'password': password}
    url = 'https://w3.gamehost.cl/dologin.php'

    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')

    entrada = inicio.find(menuitemname="Client Details")
    if entrada == None:
        print("Pass incorrecta")
    else:
        print("dentrop")


# ---------------------------------------------------------------------------------------------

#LEER UN ARCHIVO
# file1 = open('prueba.txt', 'r')
# Lines = file1.readlines()
# line = []
# for i in range(len(Lines)):
#     line.append(Lines[i].split(','))
#     line[-1][1] = re.sub("\\n","",line[-1][1])
    
# print(line)



# SIGN IN

def register(s, email, password):
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
    credenciales = {
        'nombre': 'nadie',
        'lastname':'ghola',
        'email':email,
        'numero':'23546765',
        'direccion':'calle falsa',
        'ciudad':'chimbarongo',
        'state':'chile',
        'password':password
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
    inicio = BeautifulSoup(r.content, 'html.parser')
    entrada = inicio.find(menuitemname="Client Details")
    print(entrada)


# for i in range(len(line)):
#     register(line[i][0],line[i][1])

# print('-----------------------------------')
register(s,'capulini23@gmail.com', 'javi26')
# Restablecimiento de contrasena ( sin log in)

def reset(s, email, newpass):
    resetUrl = 'https://w3.gamehost.cl/pwreset.php'
    reset = s.get(resetUrl)
    # TOKEN
    inicio = BeautifulSoup(reset.content, 'html.parser')
    token = inicio.find('script')
    accessToken = re.search('var csrfToken = (?P<token>.*)', token.string)
    print(token)
    token = accessToken.group('token')
    characters = ",'"

    for x in range(len(characters)):
        token = token.replace(characters[x],"")


    print(token)
    payload = {
        'token':token,
        'action':'reset',
        'email':email
    }
    reset = s.post(resetUrl, payload)
    payload = {
        'token':token,
        'key':"",
        'newpw':newpass,
        'confirmpw':newpass,
        'submit':'Guardar+Cambios'
    }
    resetUrl = 'https://w3.gamehost.cl/pwreset.php?action=pwreset'
    reset = s.post(resetUrl, payload)
    

    inicio = BeautifulSoup(reset.content, 'html.parser')
    
    bueno = inicio.find_all('div', class_="alert alert-success text-center")
    
    if len(bueno)!=0:
        print(bueno)
    else:
        print(inicio)



# Restablecimiento de contrasena ( CON log in) 
def resetwl( password, newpass):
    
    
    resetUrl = 'https://w3.gamehost.cl/clientarea.php?action=changepw'
    reset = s.get(resetUrl)

    # TOKEN
    inicio = BeautifulSoup(reset.content, 'html.parser')
    token = inicio.find('script')
    accessToken = re.search('var csrfToken = (?P<token>.*)', token.string)
    print(token)
    token = accessToken.group('token')
    characters = ",'"

    for x in range(len(characters)):
        token = token.replace(characters[x],"")


    print(token)

    payload = {
        'token':token,
        'submit':'true',
        'existingpw':password,
        'newpw':newpass,
        'confirmpw':newpass
    }

    reset = s.post(resetUrl, payload)
    inicio = BeautifulSoup(reset.content, 'html.parser')
    
    bueno = inicio.find_all('div', class_="alert alert-success text-center")
    malo = inicio.find_all('div', class_="alert alert-danger")
    if len(bueno)!=0:
        print(bueno)
    elif len(inicio)!=0:
        print(malo)
    else:
        print(inicio)
        
    

# inicio('capulini@gmail.com', 'AziKBrzWv8')
# resetwl( 'AziKBrzWv8', 'h')

    
