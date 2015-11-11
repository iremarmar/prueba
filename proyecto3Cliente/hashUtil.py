import hashlib


def calculaHash(mensaje,clave,index):
    m=mensaje.encode(encoding='utf_8', errors='strict')
    #Añadimos a la clave la misma numeración que el cliente para que ambas claves coincidan
    claveIndex= clave+"/"+index.__str__()
    print('Clave con indice: '+claveIndex)
    c=claveIndex.encode(encoding='utf_8', errors='strict')
    mac= m+c
    #Ciframos mensaje y clave usando el algoritmo sha256
    hash=hashlib.sha256()
    hash.update(mac)
    hashEncode = hash.hexdigest()
    return hashEncode