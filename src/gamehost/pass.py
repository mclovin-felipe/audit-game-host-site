from random import choice


def generar(email, largo):
    longitud = largo
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    p = email+','+p+'\n'
    return p
file1 = open('myfile.txt', 'w')

for i in range(1):
    
    
    file1.writelines(generar('capulini123@gmail.com', 1000))

file1.close()