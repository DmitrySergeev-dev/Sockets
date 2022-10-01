# это исходный синхронно работающий сокет initial_sync_socket после рефакторинга

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket: socket.socket):
    while True:
        print("Before .accept()")
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)
        send_message(client_socket=client_socket)


def send_message(client_socket: socket.socket):
    while True:
        print("Before .recv()")
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = "Hello, Dmitry!\n".encode()
            client_socket.send(response)
    print("Outside inner loop while")
    client_socket.close()

if __name__ == '__main__':
    accept_connection(server_socket=server_socket)
