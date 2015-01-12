import socket
import time

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('0.0.0.0', 9999))
server_sock.listen(100)

while True:
	(cli_socket, address) = server_sock.accept()
	if cli_socket.send(time.ctime(time.time()) + '\n') == 0:
		print "Client connection is broken"
	cli_socket.close()
