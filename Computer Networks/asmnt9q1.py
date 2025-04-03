# Server
import socket

def start_arp_server():
    # ARP table: IP to MAC mappings
    arp_table = {
        '192.168.1.1': '00:1A:2B:3C:4D:5E',
        '192.168.1.2': '00:1A:2B:3C:4D:5F',
        '192.168.1.3': '00:1A:2B:3C:4D:60',
    }

    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("ARP Server is running...")

    while True:
        # Receive ARP request from client
        data, client_addr = server_socket.recvfrom(1024)
        ip_requested = data.decode()
        print(f"\nReceived ARP request for IP: {ip_requested} from {client_addr}")

        # Lookup MAC address in ARP table
        mac_address = arp_table.get(ip_requested, "NOT_FOUND")

        # Send ARP reply
        server_socket.sendto(mac_address.encode(), client_addr)
        print(f"Sent ARP reply: {ip_requested} -> {mac_address} to {client_addr}")

if __name__ == "__main__":
    start_arp_server()

# Client
import socket

def start_arp_client():
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    while True:
        # Get IP address from user
        ip_address = input("\nEnter IP address to resolve (or 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            break

        # Send ARP request
        print(f"Sending ARP request for IP: {ip_address}")
        client_socket.sendto(ip_address.encode(), server_address)

        # Receive ARP reply
        data, _ = client_socket.recvfrom(1024)
        mac_address = data.decode()
        
        if mac_address == "NOT_FOUND":
            print(f"ARP Reply: MAC address not found for IP {ip_address}")
        else:
            print(f"ARP Reply: IP {ip_address} -> MAC {mac_address}")

    client_socket.close()

if __name__ == "__main__":
    start_arp_client()
