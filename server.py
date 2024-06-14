import socket
import threading

SRV_ADDR = ("127.0.0.1", 8008)
clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(2048).decode("utf-8")
            if message:
                print(f"Received: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SRV_ADDR)
    server.listen(100)
    print(f"Server started on {SRV_ADDR}")

    while True:
        client_socket, client_addr = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()