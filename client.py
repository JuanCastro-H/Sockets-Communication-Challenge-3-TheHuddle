#=====================================================
# BLOQUE 1: Librerias
#=====================================================
import socket    # Libreria que nos proporciona una interfaz de bajo ivel para la creacion de procesos de conexion
import threading # permite ejecutar varias cosas al mismo tiempo en este caso leer y escribir sin que una bloquee a la otra
import time      # Libreria que importa herramientos de tiempo para interactuar con el programa


#====================================================
# BLOQUE 2: CONFIGURACION DEL SERVIDOR
#====================================================
HOST = 'localhost' # te conecta a la misma computadora en donde corre el servidor
PUERTO = 8000      # este es el canal de comunicacion 
MAX_INTENTOS  = 10
TIEMPO_ESPERA = 2