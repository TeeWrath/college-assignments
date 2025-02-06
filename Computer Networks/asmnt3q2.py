# Server code
import socket

port = 50000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))

print(f"Socket bound to {port}")

server.listen(2)
print("Server is listening...")

conn, addr = server.accept()
print(f"Got connection from {addr}")

while True:
    received_data = conn.recv(2048).decode()
    if received_data.lower() == 'bye':
        print("Client disconnected.")
        break
    
    print(f"Message from client: {received_data}")
    
    # Check if the length of the message is even or odd
    if len(received_data) % 2 == 0:
        # (0-based index)
        response = ''.join([received_data[i] for i in range(0, len(received_data), 2)])
    else:
        response = ''.join([received_data[i] for i in range(1, len(received_data), 2)])
    
    # Send the response back to the client
    conn.send(response.encode())

print("CONNECTION CLOSED FROM THE CLIENT")
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
    client.send(data.encode())  # Send the message
    
    received_data = client.recv(2048).decode()
    print(f"Received from server: {received_data}")
    
    if data.lower() == 'bye':
        break

print("CONNECTION CLOSED FROM THE SERVER")

client.close()
