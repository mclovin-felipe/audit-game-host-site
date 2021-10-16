import requests
from bs4 import BeautifulSoup
import functions

def resetwp(sesion, passnueva):
    resetUrl = 'https://w3.gamehost.cl/clientarea.php?action=changepw'
    reset = sesion.get(resetUrl)
    token = functions.token(reset.content)
    token = functions.replace(",'", token)
    payload = {
    'token':token,
    'submit':'true',
    'existingpw':'javi2602',
    'newpw':'passnueva',
    'confirmpw':'passnueva'
    }

    reset = sesion.post(resetUrl, payload)

    print(reset.text)