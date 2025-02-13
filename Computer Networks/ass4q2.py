# Client
import socket

port = 50000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((host,portClient))

client.connect((host,port))

while True:
    data = input("Enter your message (binary data): ")
    client.send(data.encode())

    recd = client.recv(2048).decode()
    print(f"Received from the server: {recd}")

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
    data = conn.recv(2048).decode()
    if data.lower() == 'quit':
        print("Client disconnected")
        break
    print(f"Message received from client: {data}")

    # Keeping a count variable
    cnt = 0
    for i in data:
        if i == '1':
            cnt += 1
    
    # Send data back to client
    conn.send(str(cnt).encode())

print("CONNECTION CLOSED FROM THE CLIENT")
conn.close()
