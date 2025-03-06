# Server
import socket

def get_processed_string(message):
    if message.lower() == 'bye':
        return 'bye'
    
    length = len(message)
    if length % 2 == 0:  # Even length
        # Return characters at even positions (0, 2, 4, ...)
        return ''.join(message[i] for i in range(0, length, 2))
    else:  # Odd length
        # Return characters at odd positions (1, 3, 5, ...)
        return ''.join(message[i] for i in range(1, length, 2))

# Create UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9999)
server_socket.bind(server_address)

print("UDP Server is running...")

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Received from client: {message}")
    
    # Process the message
    response = get_processed_string(message)
    print(f"Sending back: {response}")
    
    # Send response back to client
    server_socket.sendto(response.encode(), client_address)
    
    if message.lower() == 'bye':
        print("Closing server...")
        break

server_socket.close()

# Client
import socket

# Create UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9999)

print("UDP Client is running...")
print("Enter 'bye' to exit")

while True:
    # Get input from user
    message = input("Enter message to send: ")
    
    # Send message to server
    client_socket.sendto(message.encode(), server_address)
    
    # Receive response from server
    data, _ = client_socket.recvfrom(1024)
    response = data.decode()
    print(f"Received from server: {response}")
    
    # Check if message is 'bye'
    if message.lower() == 'bye':
        print("Closing client...")
        break

client_socket.close()
