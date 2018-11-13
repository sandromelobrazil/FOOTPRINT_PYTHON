import socket
target = "www.google.com"
ip = socket.gethostbyname(target)

print("IP correspondente ao endereco: " + target + " eh -> " + ip)


