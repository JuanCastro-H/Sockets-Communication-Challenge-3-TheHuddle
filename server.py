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


#=======================================================
# BLOQUE 3: CREACION Y CONFIGURACION DEL SOCKET SERVIDOR
#=======================================================

# Creamos un sokect con conexiones IPV4 como puertos de 192.168.0.1  y del tipo TCP 
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# configurar las opcion internsa del socket. sol socket nivel donde se aplica la opcion a nivel de socket no del protoclo, en el servidor para reutilizar el host y puerto 
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servidor.bind((HOST, PUERTO)) # Asocia el socket a una direccion IP y Puerto (con .bind)


servidor.listen()
# basicamente le dice al sistema, estoy listo para recibir conexiones, empieza a escuchar modo servidor pasivo, pero aun no acepta ninguna conexion

# Imprime en el chat del servidor los datos del puerto y anfritrion
print(f"[🎧] Servidor escuchando en {HOST}:{PUERTO}")


#=====================================================
# BLOQUE 4: LISTA DE SOCKETS QUE EL SERVIDOR ESTA MANEJANDO
#=====================================================
clientes = [servidor] 


#=====================================================
# BLOQUE 5: BUCLE PRINCIPAL DEL SERVIDOR
# SELECT Y MANEJO DE EVENTOS
#=====================================================

while True:  # Bucle que mantiene vivo el servidor


        #---------------------------------
        # El corazon del servidor
        #---------------------------------

        # select.select basicamente le pregunta al sistema cuando un socket este listo para hacer algo
        sockets_listos, _, excepciones = select.select(clientes, [], clientes)
#        ↑               ↑               ↑
#        |               |               └── Lista de sockets con errores o estados excepcionales.
#        |               └────────────────── Lista de sockets "listos para escribir" (DESCARTADA).
#        └────────────────────────────────── Lista de sockets "listos para leer" (incluye servidor y clientes).

        #------------------------------------------------
        # Manejo de conexiones nuevas y sockets listos
        #------------------------------------------------

        for sock in sockets_listos:
            if sock == servidor: # Hay una nueva conexcion entrante
                cliente_socket, direccion = servidor.accept()
                # acepts acepta la conexion y se crea un nuevo socket exclusivo para este cliente (cliente socket) y se guarda su direccion IP en la variable direccion
    
                clientes.append(cliente_socket) # Agrega el nuevo sokect del cliente en la lista vacia de clientes
                print(f"[+] Nuevo cliente conectado desde {direccion}")