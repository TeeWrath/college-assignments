# Client
import socket

port = 50000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((host,portClient))

client.connect((host,port))

while True:
    data = input("Enter your message: ")
    client.send(data.encode())

    received_data = client.recv(2048).decode()
    print(f"Received from server: {received_data}")

    if data.lower() == 'quit':
        break

print("CONNECTION CLOSED FROM THE SERVER")
client.close()

# Server
import socket

port = 50000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind((host,port))

print(f"Socket bound to {port}")

server.listen(2)
print("Server is listening...")

conn, addr = server.accept()
print(f"got connection from {addr}")

while True:
    received_data = conn.recv(2048).decode()
    if received_data.lower() == 'quit':
        print("Client disconnected.")
        break
    print(f"Message received from client : {received_data}")

    # Storing the number received
    num = int(received_data)
    sum = 0 # To store sum
    for i in range(1,num + 1,1):
        sum = sum + (i*i)

    # Sending the data back
    conn.send(str(sum).encode())

print("CONNECTION CLOSED FROM THE CLIENT")
conn.close()
