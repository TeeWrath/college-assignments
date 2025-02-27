# Server
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

def checkIfPalindrome(expression):
	exp = expression.strip().replace(" ", "").lower()  # Remove spaces and convert to lowercase
	return exp == exp[::-1]  # Check if reversed string is the same

while True:
	data = conn.recv(2048).decode().strip()  # Receive message from client
	if not data:
    	break  # No data received, break out of the loop
    
	if data.lower() == 'quit':  # If the client sends 'quit', terminate the loop
    	print("Client disconnected")
    	break
    
	print(f"Message received from client: {data}")

	try:
    	result = "Palindrome" if checkIfPalindrome(data) else "Not a Palindrome"
    	conn.sendall(result.encode('utf-8'))
	except Exception as e:
    	error_message = f"Error: {str(e)}"
    	conn.sendall(error_message.encode('utf-8'))

print("Connection closed from the client.")
conn.close()
server.close()

# Client
import socket

port = 50000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((host,portClient))

client.connect((host,port))

while True:
	data = input("Enter your message (a string):")
	client.send(data.encode())

	recd = client.recv(2048).decode()
	print(f"Received from the server: {recd}")

	if data.lower() == 'quit' :
    	break

print("CONNECTON CLOSED FROM THE SERVER")
client.close()
