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

#Server
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

# Function to evaluate a postfix expression using a stack
def evaluate_postfix(expression):
    stack = []
    
    # Loop through each character in the postfix expression
    for char in expression.split():
        if char.isdigit():  # If the character is a number, push it to the stack
            stack.append(int(char))
        else:
            # If the character is an operator, pop two operands and apply the operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            else:
                raise ValueError(f"Unknown operator: {char}")
            
            # Push the result back to the stack
            stack.append(result)
    
    return stack.pop()

while True:
    data = conn.recv(2048).decode()  # Receive message from client
    if not data:
        break  # No data received, break out of the loop
    
    if data.lower() == 'quit':  # If the client sends 'quit', terminate the loop
        print("Client disconnected")
        break
    
    print(f"Message received from client: {data}")

    try:
        # Evaluate the postfix expression
        result = evaluate_postfix(data)
        # Send the result back to the client
        conn.sendall(str(result).encode('utf-8'))
    except Exception as e:
        # Send error message if the expression is invalid
        error_message = f"Error: {str(e)}"
        conn.sendall(error_message.encode('utf-8'))

print("Connection closed from the client.")
conn.close()
server.close()
