# 🌐 Conexión 0 — Network Programming with Sockets

> "Every connection begins with a single packet."

A client-server networking project built with Python sockets that allows multiple clients to communicate in real time through a central TCP server.

---

# 🎬 Description

This project implements a low-level network communication system using Python sockets.

The architecture consists of:

- A central TCP server
- Multiple concurrent clients
- Real-time message broadcasting
- Automatic reconnection handling
- Non-blocking I/O with `select`

The system demonstrates the foundations of network programming and how communication protocols work internally.

---

## 🎯 Objective

Build a practical networking system capable of:

- Creating TCP socket connections
- Managing multiple clients simultaneously
- Broadcasting messages in real time
- Handling disconnections safely
- Reconnecting clients automatically
- Practicing concurrent network programming

---

## ⚙️ Technologies Used

- Python
- socket
- select
- threading
- TCP/IP

---

## 🏗️ Project Structure

```text
conexion-0/

server/
server.py

client/
client.py
```

---

## ⚙️ How It Works

### Server

The server:

- Creates a TCP socket
- Listens for incoming clients
- Uses `select.select()` to manage multiple connections
- Receives and broadcasts messages
- Detects client disconnections

### Client

The client:

- Connects to the server
- Sends messages from the console
- Receives messages in real time
- Uses threads for concurrent communication
- Reconnects automatically if connection is lost

---

## 🧩 Key Features

✔ Real-time communication  
✔ Multiple simultaneous clients  
✔ Automatic reconnection system  
✔ Concurrent message handling  
✔ Broadcast messaging  
✔ TCP/IP socket implementation  

---

## 🚀 Usage

### Start the server

```bash
python server.py
```

### Run one or more clients

```bash
python client.py
```

---

## 📈 Possible Improvements

- Private messaging
- User nicknames
- Chat rooms
- Encrypted communication
- File transfer support
- AsyncIO implementation

---

## 👨‍💻 Author

**Juan Castro**

---

# 📌 Resumen en Español

Este proyecto implementa un sistema cliente-servidor utilizando sockets TCP en Python.

Permite que múltiples clientes se conecten a un servidor central para intercambiar mensajes en tiempo real.

---

## 🎯 Objetivo

Practicar conceptos fundamentales de programación de red:

- Comunicación mediante sockets
- Arquitectura cliente-servidor
- Concurrencia
- Manejo de múltiples conexiones
- Reconexión automática

---

## ⚙️ Funcionamiento

### Servidor

El servidor:

- Escucha conexiones entrantes
- Maneja múltiples clientes con `select`
- Recibe mensajes
- Los reenvía al resto de clientes

### Cliente

El cliente:

- Se conecta al servidor
- Envía mensajes desde consola
- Recibe mensajes en tiempo real
- Usa threads para lectura y escritura concurrente
- Se reconecta automáticamente si pierde conexión

---

## 🚨 Características Destacadas

- Comunicación en tiempo real
- Múltiples clientes simultáneos
- Reconexión automática
- Broadcast de mensajes
- Servidor no bloqueante

---

## 🧠 Conclusión

El proyecto demuestra cómo construir un sistema de comunicación en red utilizando sockets TCP y concurrencia en Python.

Funciona como una introducción práctica a conceptos utilizados en:

- chats
- videojuegos online
- aplicaciones cliente-servidor
- sistemas distribuidos