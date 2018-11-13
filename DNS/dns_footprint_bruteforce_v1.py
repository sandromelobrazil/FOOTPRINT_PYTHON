import socket
target = "yahoo.com"

with open('wordlist', 'r') as MACHINES:
    print(MACHINES)

    while True:
        MACHINE = MACHINES.readline().strip("\n")
        
        if not MACHINE:
            break 

        MACHINE = MACHINE + "." + target
        try:
            print(MACHINE + ": " + socket.gethostbyname(MACHINE))
        except socket.gaierror: 
            pass


