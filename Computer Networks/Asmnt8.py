# Server
import socket
import threading

def handle_client(client_socket, address):
    """Handle individual client connections"""
    print(f"New connection from {address}")
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:  # If client disconnects
                break
                
            print(f"Message from {address}: {message}")
            # Echo message back to client
            client_socket.send(f"Server echo: {message}".encode('utf-8'))
            
        except:
            break
    
    print(f"Connection closed from {address}")
    client_socket.close()

def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Server configuration
    HOST = 'localhost'  # or '127.0.0.1'
    PORT = 5555
    
    # Bind and listen
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        try:
            # Accept new connections
            client_socket, address = server_socket.accept()
            # Create new thread for each client
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address)
            )
            client_thread.start()
            
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            break
    
    server_socket.close()

if __name__ == "__main__":
    start_server()

# Client
import socket
import threading
import time

def receive_messages(client_socket):
    """Thread to handle receiving messages from server"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
        except:
            break

def start_client():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow port reuse
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Server configuration
    HOST = 'localhost'
    PORT = 5555
    
    try:
        # Connect to server
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        
        # Start receiving thread
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,)
        )
        receive_thread.start()
        
        # Main loop for sending messages
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            
            client_socket.send(message.encode('utf-8'))
            time.sleep(0.1)  # Small delay to prevent message overlap
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()
