#=====================================================
# BLOQUE 1: Librerias
#=====================================================
import socket    # Libreria que nos proporciona una interfaz de bajo ivel para la creacion de procesos de conexion
import threading # permite ejecutar varias cosas al mismo tiempo en este caso leer y escribir sin que una bloquee a la otra
import time      # Libreria que importa herramientos de tiempo para interactuar con el programa


#====================================================
# BLOQUE 2: CONFIGURACION DEL SOCKET
#====================================================
HOST = 'localhost' # te conecta a la misma computadora en donde corre el servidor
PUERTO = 8000      # este es el canal de comunicacion 
MAX_INTENTOS  = 10
TIEMPO_ESPERA = 2


#====================================================
# BLOQUE 3: CREACION DEL SOCKET CLIENTE Y CONEXION
#====================================================

def conectar(): 

    intento = 1
    while intento <= MAX_INTENTOS: # Bucle de conexion con el servidor
        
        try:
            # --- Creacion del socket Y Asociacion Puerto/IP ---
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un objeto socket de la clase socket con los protocolos IPv4 (AF_INET) y TCP (SOCK_STREAM)
            cliente.connect((HOST, PUERTO)) # Conecta el sokect cliente al sevidor con la IP y puerto indicados

            print(f"[✅ ] Conectado al servidor en el intento {intento}.")
            return cliente # Si se conecta, sale del bucle)
            
        except ConnectionRefusedError:
            print(f"[⚠️ ] Intento {intento} fallido. Reintentando en 2 segundos...")
            intento += 1
            time.sleep(2)

    else:
        print("[❌ ] No se pudo establecer la conexion con el servidor.")
        cliente.close()
        return None
    

#====================================================
# BLOQUE 4: FUNCION PARA RECIBIR MENSAJES
#====================================================
def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode() # Recibe hasta 1024 bytes del servidor y los transforma a texto legible
            if not mensaje: # Si el mensaje esta vacio termina la funcion (Perdida de conexion)
                break
            print(f"\n🐙 {mensaje}")
        except:             # Si captura erroes...
            print("\n[⚠️ ] Conexión perdida con el servidor.")
            cliente.close() # Cierra el servidor
            break


#=============================================================================================
# BLOQUE 5: FUNCION PARA ENVIAR MENSAJES
#=============================================================================================
def enviar_mensajes(cliente):
    while True:
        try:
            mensaje = input()              # Recibe el texto del mensaje desde la consola
            cliente.send(mensaje.encode()) # Envia el mensaje codificado en Bytes al servidor
        except:
            break # Si ocurre un error termina la funcion