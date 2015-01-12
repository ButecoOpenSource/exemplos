import socket

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect(('127.0.0.1', 9999))

print cli_socket.recv(255)

cli_socket.close()
