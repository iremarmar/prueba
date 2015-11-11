import hashlib
from random import getrandbits
from _struct import unpack, calcsize

def calculaClave(g, primo, n):
    res = pow(g, n, primo)
    return res

def generaPrimo():
    return 9392

def dhe(sc):
    # Obtenemos clave  con Diffie-Hellman Efímero
    n = getrandbits(32)
    primo = generaPrimo()
    B = calculaClave(2, primo, n)
    # Mandamos al cliente la primera parte de la clave
    B = B.__str__().encode('utf-8')
    sc.send(B)   
    print(B)
    # Recibimos del cliente su primera parte de la clave
    recibido = sc.recv(1024)
    A = int(recibido.decode())
    print('A: ' + A.__str__())
    # Generamos clave secreta con la clave del cliente y la nuestra 
    key = calculaClave(A, primo, n)
    print('key: ' + key.__str__())
    return key
