import socket
target = "yahoo.com"

with open('wordlist', 'r') as MACHINES:
    print(MACHINES)

    LISTA = MACHINES.readline().strip("\n")
    
    for MACHINE in LISTA: 
        if not MACHINE:
            break 

        MACHINE = MACHINE + "." + target
        try:
            print(MACHINE + ": " + socket.gethostbyname(MACHINE))
        except socket.gaierror: 
            pass


