# Client
import socket

    # Define server address and port (must match server's)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
    
    # Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
while True:
    # Get message from user
    message = input("Enter message to send (or 'quit' to exit): ")
    client_socket.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
    if message.lower() == 'quit':
        print("Closing the Client \n")
        break

# Closing CLient
client_socket.close()

# Server
import socket

# Create a UDP server
SERVER_HOST = '127.0.0.1'  # localhost
SERVER_PORT = 5000
    
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
# Bind the socket to address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))
    
print(f"UDP Server running on {SERVER_HOST}:{SERVER_PORT}")
print("Waiting for messages...")
    
while True:
    # Receive message from client (buffer size is 1024 bytes)
    data, client_address = server_socket.recvfrom(1024)
            
    # Decode and display the received message
    message = data.decode('utf-8')
    print(f"Message from {client_address}: {message}")
    if message.lower() == 'quit':
        print("Closing Server...")
        break

# Close the socket outside the loop
server_socket.close()
