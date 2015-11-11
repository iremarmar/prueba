import hashlib
from random import getrandbits
import socket
import time
import acuerdoClaves
import hashUtil


#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("127.0.0.1", 7071))
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(1)
#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
(sc, addr) = s.accept()

#Este indice nos sirve para que solo se realice el acuerdo una vez por cada conexión
i=1

while True:
    
    if i==1:
        key = acuerdoClaves.dhe(sc)
        i-=1
    #Recibimos mensaje del cliente
    recibido = sc.recv(1024)
    recibido = recibido.decode()
    print(recibido)
    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":    
        break
 
    else:
        index = 0
        mensaje = recibido.split('-')
        hashMensaje = hashUtil.calculaHash(mensaje[0],key.__str__(),index)
        if hashMensaje==mensaje[1]:
            ok = 'Mensaje recibido integramente'
            #Enviamos respuesta al cliente 
            sc.send(ok.encode(encoding='utf_8', errors='strict'))
        else:
            corrupto = 'Mensaje corrupto'
            #Enviamos respuesta al cliente 
            sc.send(corrupto.encode(encoding='utf_8', errors='strict'))
            #Escribimos en un fichero log los mensajes corruptos
            outfile = open('C:\\Users\\Irene\\Documents\\UNIVERSIDAD\\log.txt','a')
            outfile.write(time.strftime("%d/%m/%y")+' - '+ time.strftime("%H:%M:%S")+' '+corrupto+': '+mensaje[0]+'\r\n' )
        mensaje = recibido
    index+=1
        
print ("Adios.")
 
#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()