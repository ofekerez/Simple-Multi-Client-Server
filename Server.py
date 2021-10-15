import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8200))
server_socket.listen(1000)


def handle_client(client: socket.socket, client_number: int):
    while True:
        data = client_socket.recv(2048).decode()
        print(f"Client {client_number}:", data)
        if data == 'exit':
            client_socket.close()
            break
        # Server_Answer = input("Enter your Answer ")
    #    client_socket.send(Server_Answer.encode())

counter = 1
while True:
    client_socket, client_address = server_socket.accept()
    print("A new client,  client {0} has connected from the IP address of:".format(counter))
    th = threading.Thread(target=handle_client, args=(client_socket, counter), daemon=True)
    th.start()
    counter += 1
