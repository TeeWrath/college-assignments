# Server
import socket

def start_rarp_server():
    # RARP table: MAC to IP mappings
    rarp_table = {
        '00:1A:2B:3C:4D:5E': '192.168.1.1',
        '00:1A:2B:3C:4D:5F': '192.168.1.2',
        '00:1A:2B:3C:4D:60': '192.168.1.3',
        'A4:6E:A4:57:82:56': '141.14.56.21'  # From the document example
    }

    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 12346))
    print("RARP Server is running...")

    while True:
        # Receive RARP request from client
        data, client_addr = server_socket.recvfrom(1024)
        mac_requested = data.decode()
        
        # Check for exit command
        if mac_requested.lower() == 'exit':
            print("\nReceived shutdown command. Closing server...")
            server_socket.close()
            return

        print(f"\nReceived RARP request for MAC: {mac_requested} from {client_addr}")

        # Lookup IP address in RARP table
        ip_address = rarp_table.get(mac_requested, "NOT_FOUND")

        # Send RARP reply
        server_socket.sendto(ip_address.encode(), client_addr)
        print(f"Sent RARP reply: {mac_requested} -> {ip_address} to {client_addr}")

if __name__ == "__main__":
    start_rarp_server()

# Client

import socket

def start_rarp_client():
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12346)

    while True:
        # Get MAC address from user
        mac_address = input("\nEnter MAC address to resolve (or 'exit' to quit): ")
        
        # Send request
        client_socket.sendto(mac_address.encode(), server_address)
        
        if mac_address.lower() == 'exit':
            print("Sent server shutdown command")
            break

        print(f"Sending RARP request for MAC: {mac_address}")

        # Receive RARP reply
        data, _ = client_socket.recvfrom(1024)
        ip_address = data.decode()
        
        if ip_address == "NOT_FOUND":
            print(f"RARP Reply: IP address not found for MAC {mac_address}")
        else:
            print(f"RARP Reply: MAC {mac_address} -> IP {ip_address}")

    client_socket.close()

if __name__ == "__main__":
    start_rarp_client()
