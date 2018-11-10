import socket
target = "8.8.4.4"
ip = tuple(socket.gethostbyaddr(target))
ip2 = ip[0]

print("O nome correspondente ao endereco IP : " + target + " eh -> " + ip2 )


