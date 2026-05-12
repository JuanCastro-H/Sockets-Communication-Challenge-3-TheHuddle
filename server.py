#=====================================================
# BLOQUE 1: LIBRERIAS
#=====================================================
import socket # Libreria que proporciona las funciones y clases necesarias para crear y manipular sockets
import select # Función que permite vigilar múltiples sockets simultaneamente para realizar alguna operación (leer, escribir o detectar errores), sin necesidad de usar hilos.


#=====================================================
# BLOQUE 2: CONFIGURACION INICIAL
#=====================================================
HOST = 'localhost' # 127.0.0.1
PUERTO = 8000 # para desarrollo local aunque es conocido como puerto utilizado por malware, podria utilizarse el piuerto 8000