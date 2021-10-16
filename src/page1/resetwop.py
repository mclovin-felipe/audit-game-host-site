import requests
from bs4 import BeautifulSoup
import functions


def resetwop(sesion, passnueva):
    resetUrl = 'https://w3.gamehost.cl/pwreset.php'
    reset = sesion.get(resetUrl)
    token = functions.token(reset.content)
    token = functions.replace(",'", token)
    payload = {
        'token':token,
        'action':'reset',
        'email':'fponcecanales@gmail.com'
    }
    reset = sesion.post(resetUrl, payload)
    payload = {
        'token':token,
        'key':"",
        'newpw':passnueva,
        'confirmpw':passnueva,
        'submit':'Guardar+Cambios'
    }
    resetUrl = 'https://w3.gamehost.cl/pwreset.php?action=pwreset'
    reset = sesion.post(resetUrl, payload)

    print(reset.text)
