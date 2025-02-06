# Server code
import socket

port = 50000

host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))

print("Socket binded to %s" %(port))

server.listen(2)

print("socket is listening...")

conn,addr = server.accept()

print("got connection from", addr)

while True:
    recieved_data = conn.recv(2048)
    print("Message from client:", recieved_data.decode())
    if recieved_data.decode() == 'quit':
        break

print("connection closed from client")
conn.close()

# Client code
import socket

port = 50000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((host, portClient))

client.connect((host, port))

while True:
    data = input("Enter your message: ")
    client.send(data.encode()) 
    if data == 'quit': 
        break

print("CONNECTION CLOSED FROM THE SERVER")

client.close()
