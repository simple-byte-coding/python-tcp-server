import socket
import threading

IP = "127.0.0.1"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    server.bind((IP, PORT))
    server.listen(5)
    print(f"Listening on {IP}:{PORT}...")

    while True:
        client, client_info = server.accept()
        print(f"We have a connection!")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'Recieved: {request.decode("utf-8")}')
        sock.send(b"ACK")
        sock.close()


if __name__ == "__main__":
    main()
