import requests
from bs4 import BeautifulSoup


def login(sesion):
    


    payload = {'username': 'fponcecanales@gmail.com', 'password': 'javi2602'}
    url = 'https://w3.gamehost.cl/dologin.php'

    r = sesion.post(url, data=payload)
    # r =requests.post(url, data=payload)
    inicio = BeautifulSoup(r.content, 'html.parser')

    entrada = inicio.find(menuitemname="Client Details")
    if entrada == None:
        print("Pass incorrecta")
    else:
        print("dentrop")
