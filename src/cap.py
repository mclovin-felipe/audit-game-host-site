# import numpy as np
# import cv2

# #Leer una imagen
# img = cv2.imread('image.png')

# #Cambiar el espacio de color en img2
# img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY )

# #Imprimo características de la imagen en su nuevo espacio de color
# # alto, ancho y canales
# print("alto, alto, canales = "+ str(img2.shape))

# with open('test.png', 'wb') as file:
#     file.write(img2)

import cv2
import numpy as np


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


