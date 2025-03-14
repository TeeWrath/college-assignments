# server
import socket
import requests

# Define server address and port
HOST = "127.0.0.1"  # Change if needed
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server started. Listening on {HOST}:{PORT}...")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    try:
        # Receive URL from client
        url = client_socket.recv(1024).decode()
        print(f"Fetching URL: {url}")

        # Fetch the webpage
        response = requests.get(url)
        webpage_content = response.content

        # Send content to client
        client_socket.sendall(webpage_content)

    except Exception as e:
        print("Error:", e)
        client_socket.send(b"Failed to fetch the webpage.")

    finally:
        # Close client connection
        client_socket.close()

# Client
import socket

# Define server address and port
SERVER_IP = "127.0.0.1"  # Change if needed
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to server.")

    # Get URL from user
    url = input("Enter the URL to fetch: ")
    client_socket.send(url.encode())

    # Receive webpage content
    response = b""
    while True:
        data = client_socket.recv(4096)  # Receive data in chunks
        if not data:
            break
        response += data

    # Save received data to a file
    with open("downloaded_page.html", "wb") as file:
        file.write(response)
    
    print("Webpage saved as 'downloaded_page.html'.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the connection
    client_socket.close()

