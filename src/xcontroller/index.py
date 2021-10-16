import requests
from bs4 import BeautifulSoup
from bs4 import Comment
s = requests.Session()
def login(s):
    payload = {'username': "fponcecanales@gmail.com", 'password': 'javi2602@','woocommerce-login-nonce':'c190cdf0c1','_wp_http_referer':'/mi-cuenta/', 'login':'Acceder'}
    url = 'https://xcontrollers.es/mi-cuenta/'

    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    print(inicio)
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    #entrada = inicio.find(id="username")
    
    comments = comments[-1]
    comments = comments.find('User is logged in')
    if comments == -1:
        print("Pass incorrecta")
    else:
        print(comments)
        print("dentrop")

#username=fponcecanales%40gmail.com&
# password=javi2602%40&
# woocommerce-login-nonce=c190cdf0c1&
# _wp_http_referer=%2Fmi-cuenta%2F&
# login=Acceder

   
   
#register
def register(s):
    payload = {'username': "fponcecanales@gmail.com", 'password': 'javi2602@','Acepto':'1','woocommerce-login-nonce':'1383879d98','_wp_http_referer':'/mi-cuenta/', 'login':'Register'}
    url = 'https://xcontrollers.es/mi-cuenta/'

    r = s.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')
    comments = inicio.find_all(string=lambda text: isinstance(text, Comment))
    #entrada = inicio.find(id="username")
    comments = comments[-1]
    comments = comments.find('User is logged in')
    if comments == -1:
        print("Pass incorrecta")
    else:
        print(comments)
        print("dentrop")

#login(s)