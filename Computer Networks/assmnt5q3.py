# Server
import socket
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth):
	"""Crawl the website up to the given depth and return found URLs."""
	visited = set()
	urls_to_crawl = [(url, 0)]  # (URL, current depth)
	crawled_urls = []

	while urls_to_crawl:
    	current_url, current_depth = urls_to_crawl.pop(0)
   	 
    	if current_url in visited or current_depth > depth:
        	continue
   	 
    	print(f"Crawling: {current_url} (Depth: {current_depth})")
    	visited.add(current_url)

    	try:
        	response = requests.get(current_url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        	if response.status_code != 200:
            	continue
    	except requests.RequestException:
        	continue
   	 
    	soup = BeautifulSoup(response.text, "html.parser")
    	crawled_urls.append(current_url)  # Store the visited URL
   	 
    	# Extract and enqueue new links
    	for link in soup.find_all("a", href=True):
        	new_url = urljoin(current_url, link["href"])
        	if new_url.startswith("http"):  # Avoid non-HTTP links
            	urls_to_crawl.append((new_url, current_depth + 1))

	return crawled_urls

def start_server(host="127.0.0.1", port=50000):
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((host, port))
	server_socket.listen(2)

	print(f"Server listening on {host}:{port}...")

	conn, addr = server_socket.accept()
	print(f"Connected to {addr}")

	while True:
    	data = conn.recv(2048).decode().strip()
    	if not data:
        	break

    	if data.lower() == "quit":
        	print("Client disconnected.")
        	break

    	try:
        	url, depth = data.split(" ", 1)
        	print(f"Received request to crawl: {url} (Depth: {depth})")
        	urls = crawl(url, int(depth))
        	response = json.dumps(urls)
    	except Exception as e:
        	response = json.dumps({"error": str(e)})

    	conn.sendall(response.encode('utf-8'))

	conn.close()
	server_socket.close()
	print("Server closed.")

if __name__ == "__main__":
	start_server()

# Client
import socket
import json

def start_client(host="127.0.0.1", port=50000):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((host, port))
	print(f"Connected to server at {host}:{port}")

	while True:
    	url = input("Enter URL to crawl (or 'Quit' to exit): ")
    	if url.lower() == "quit":
        	client_socket.send(url.encode())
        	break

    	depth = input("Enter depth: ")
    	message = f"{url} {depth}"
    	client_socket.send(message.encode())

    	response = client_socket.recv(4096).decode()
    	try:
        	urls = json.loads(response)
        	print("\nCrawled URLs:")
        	for url in urls:
            	print(url)
    	except json.JSONDecodeError:
        	print("Invalid response from server.")

	client_socket.close()
	print("Client closed.")

if __name__ == "__main__":
	start_client()
