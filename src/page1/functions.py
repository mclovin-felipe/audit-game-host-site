import re
from bs4 import BeautifulSoup
import cv2
import numpy as np
import time
import resolver

def token(content):
    # TOKEN
    inicio = BeautifulSoup(content, 'html.parser')
    token = inicio.find('script')
    accessToken = re.search('var csrfToken = (?P<token>.*)', token.string)
    print(token)
    token = accessToken.group('token')
    token = replace(",'", token)
    
    return token

def cambioColor(image):
    m =  cv2.imread(image)

    h,w,bpp = np.shape(m)

    for py in range(0,h):
        for px in range(0,w):
            if(m[py][px][0] >100):            
                m[py][px][0]=255
                m[py][px][1]=255
                m[py][px][2]=255

    cv2.imwrite('test2.png',m)

def catpcha(content):
    # CAPCHAAAAA
    with open('test.png', 'wb') as file:
        file.write(content)
    cambioColor('test.png')
    time.sleep(1)
    codigo = resolver.recognize('test2.png')
    codigo = replace(",", codigo)
    
    return codigo

def replace(signos, string):
    characters = signos

    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    return string
