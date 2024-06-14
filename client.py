import socket
import threading

SRV_ADDR = ("127.0.0.1", 8008)

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(2048).decode("utf-8")
            if message:
                print(message)
        except:
            print("An error occurred!")
            sock.close()
            break

def send_messages(sock):
    while True:
        message = input()
        try:
            sock.send(message.encode("utf-8"))
        except:
            print("An error occurred!")
            sock.close()
            break

def start_client(client_number):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(SRV_ADDR)
    print(f"Client {client_number} connected to the server")

    threading.Thread(target=receive_messages, args=(client_sock,)).start()
    send_messages(client_sock)

if __name__ == "__main__":
    import sys
    client_number = sys.argv[1] if len(sys.argv) > 1 else "Unknown"
    start_client(client_number)