import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re

s = requests.Session()
def login(s, email, password):
    
    url = 'https://xcontrollers.es/mi-cuenta/'
    r1 =s.get(url)
    inicio = BeautifulSoup(r1.content, 'html.parser')
    comments = inicio.find_all(id='woocommerce-login-nonce')
    print(str(comments[0])[88:98])
    payload = {'username': email,
               'password': password,
               'woocommerce-login-nonce':str(comments[0])[88:98],
               '_wp_http_referer':'/mi-cuenta/', 
               'login':'Acceder'}
    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    #print(inicio)
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    #entrada = inicio.find(id="username")
    
    comments = comments[-1]
    comments = comments.find('User is logged in')
    if comments == -1:
        print("Pass incorrecta")
        print(inicio)
    else:
        print(comments)
        print("dentrop")

#username=fponcecanales%40gmail.com&
# password=javi2602%40&
# woocommerce-login-nonce=c190cdf0c1&
# _wp_http_referer=%2Fmi-cuenta%2F&
# login=Acceder

   
   
#register
def register(s, email, password):
    
    url = 'https://xcontrollers.es/mi-cuenta/'
    r1 =s.get(url)
    inicio = BeautifulSoup(r1.content, 'html.parser')
    comments = inicio.find_all(id='woocommerce-register-nonce')
    payload = {'email': email,
               'password':password,
               'acepto':'1',
               'woocommerce-register-nonce':str(comments[0])[94:104],
               '_wp_http_referer':'/mi-cuenta/',
               'register':'Registrarse'}
    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    #print(inicio)
    comments = comments[-1]
    comments = comments.find('User is logged in')
    if comments == -1:
        print("Usuario existente")
    else:
        print(comments)
        print("dentrop")
def reset(s):
    payload = {'user_login': "nadie134@gmail.com",
               'wc_reset_password': 'true',
               'acepto':'1',
               '_wpnonce':'5a5f9296ad',
               '_wp_http_referer':'/mi-cuenta/lost-password/'}
    url = 'https://xcontrollers.es/mi-cuenta/'

    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    print(inicio)
    comments = comments[-1]
    comments = comments.find('Requested URI contains query')
    if comments == -1:
        print("No se envio")
    else:
        print(comments)
        print("Enviado")

def resetwpass(s, email, password, newpassword):
    login(s, email, password)
    
    url = 'https://xcontrollers.es/mi-cuenta/edit-account/'
    r1 =s.get(url)
    
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r1.content, 'html.parser')
    comments = inicio.find_all(id='_wpnonce')
    print(str(comments[0])[58:68])
    payload = {'account_first_name':'Felipe',
               'account_last_name':'Ponce',
               'account_email': email,
               'password_current': '',
               'password_1':newpassword,
               'password_2':newpassword,
               '_wpnonce':str(comments[0])[58:68],
               '_wp_http_referer':'/mi-cuenta/edit-account/',
               'save_account_details':'Guardar+los+cambios',
               'action':'save_account_details'}
    r = s.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    #entrada = inicio.find(id="username")
    
    comments = comments[-1]
    comments = comments.find('User is logged in')
    if comments == -1:
        print(inicio)
    else:
        print(comments)
        print("EXITO")
    
    # comments = comments[-1]
    # comments = comments.find('Requested URI contains query')
    # if comments == -1:
    #     print("No se envio")
    # else:
    #     print(comments)
    #     print("Enviado")
#reset(s)

#resetwpass(s)
#register(s)
#login(s)
register(s, 'capulini23@gmail.com', 'a')


# LEER UN ARCHIVO
# file1 = open('myfile.txt', 'r')
# Lines = file1.readlines()
# line = []
# for i in range(len(Lines)):
#     line.append(Lines[i].split(','))
#     line[-1][1] = re.sub("\\n","",line[-1][1])
    
# print(line)

# for i in range(len(line)):
#     login(s,line[i][0],line[i][1])
