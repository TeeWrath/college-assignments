# Server
import socket

def xor(a, b):
    """Perform XOR operation between two binary strings."""
    result = []
    min_length = min(len(a), len(b))
    for i in range(1, min_length):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result) + a[min_length:]

def mod2div(dividend, divisor):
    """Perform Modulo-2 Division."""
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor) + dividend[pick]
        else:
            tmp = xor(tmp, '0' * pick) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor(tmp, '0' * pick)

    return tmp.zfill(len(divisor)-1)

def encodeData(data, key):
    """Append CRC remainder to the data."""
    appended_data = data + '0' * (len(key) - 1)
    remainder = mod2div(appended_data, key)
    return data + remainder, remainder

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server is listening. . . .")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    received_message = conn.recv(1024).decode()
    data, key = received_message.split(',')

    print(f"Databit recieved : {data}")
    print(f"Key got = {key}")

    encoded_data, remainder = encodeData(data, key)
    
    print(f"Codeword to be sent to client : {encoded_data}")
    print(f"Remainder to be sent to client : {remainder}")

    # Send both the encoded data and the remainder
    conn.send(f"{encoded_data},{remainder}".encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()

# Client
import socket

def xor(a, b):
    """Perform XOR operation between two binary strings."""
    result = []
    min_length = min(len(a), len(b))
    for i in range(1, min_length):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result) + a[min_length:]

def mod2div(dividend, divisor):
    """Perform Modulo-2 Division."""
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor) + dividend[pick]
        else:
            tmp = xor(tmp, '0' * pick) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor(tmp, '0' * pick)

    return tmp.zfill(len(divisor)-1)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('127.0.0.1', 12345))
        
        data = input("Enter data bit sequence: ")
        key = input("Enter key: ")

        message = data + ',' + key  # Send data and divisor together
        client_socket.send(message.encode())

        # Receive both encoded data and remainder
        response = client_socket.recv(1024).decode()
        encoded_data, remainder = response.split(',')
        
        print(f"Remainder received from server: {remainder}")
        print(f"Codeword received from server: {encoded_data}")
        
        # Calculate remainder at client side for verification
        # Append zeros to data
        appended_data = data + '0' * (len(key) - 1)
        client_remainder = mod2div(appended_data, key)
        print(f"Remainder calculated at Client side: {client_remainder}")
        
        # Check if there's an error
        if remainder != client_remainder:
            print("Error is detected at Reciever Side")
        else:
            print("No Error detected")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
