import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8200))
while True:
    msg = input("Enter your message pls: ")
    client_socket.send(msg.encode())
    if msg.lower() == 'exit':
        break
