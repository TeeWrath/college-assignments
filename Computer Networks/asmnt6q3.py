# Server
import socket

def count_ones(binary_string):
    # Remove any whitespace and count '1's
    return binary_string.replace(' ', '').count('1')

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
    
    if message.lower() == 'quit':
        response = 'Server shutting down'
        server_socket.sendto(response.encode(), client_address)
        print("Closing server...")
        break
    
    # Count number of 1s and prepare response
    ones_count = count_ones(message)
    response = str(ones_count)
    print(f"Sending back: {response}")
    
    # Send response back to client
    server_socket.sendto(response.encode(), client_address)

server_socket.close()

# Client
import socket

# Create UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9999)

print("UDP Client is running...")
print("Enter binary values (e.g., 1010) or 'Quit' to exit")

while True:
    # Get input from user
    message = input("Enter binary values: ")
    
    # Send message to server
    client_socket.sendto(message.encode(), server_address)
    
    # Receive response from server
    data, _ = client_socket.recvfrom(1024)
    response = data.decode()
    
    if message.lower() == 'quit':
        print(f"Server response: {response}")
        print("Closing client...")
        break
        
    print(f"Number of 1s received from server: {response}")

client_socket.close()
