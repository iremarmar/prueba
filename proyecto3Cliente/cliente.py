import socket
from random import getrandbits
import hashlib
import ctypes
import hashUtil
import acuerdoClaves

 
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("127.0.0.1", 7071))
#Indice para que solo se realice el acuerdo de claves una vez por conexión
i=1
#Creamos un bucle para retener la conexion
while True:
    index = 0
    if i==1:
        key = acuerdoClaves.dhe(s)
        i-=1
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mensaje = input("Mensaje a enviar: ")
    envio = hashUtil.calculaHash(mensaje,key.__str__(),index)
    envio = (mensaje+'-'+envio).encode('utf-8')
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(envio)
    answer = s.recv(1024)
    answer = answer.decode()
    
    if (answer == "Mensaje recibido integramente"):
        #print(answer)
        ctypes.windll.user32.MessageBoxW(0,answer, "Aviso", 0)
    if (answer == "Mensaje corrupto"):
        #print(answer)
        ctypes.windll.user32.MessageBoxW(0,answer, "Aviso", 0)
    #Si por alguna razon el mensaje es close cerramos la conexion
    if (mensaje == "close"):
        break
 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print ("Adios.")
 
#Cerramos la instancia del objeto servidor
s.close()