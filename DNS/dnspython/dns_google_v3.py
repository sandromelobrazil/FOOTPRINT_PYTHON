import socket
google = "google.com"
nomes = ["ns" , "ns1", "ns2", "ns3", "ns4", "mx", "mx1", "mx2"  "www", "www2", "www3"]

for nome in nomes:
    MACHINE = nome + "." + google 
    try:
        print(MACHINE + ": " + socket.gethostbyname(MACHINE))
    except socket.gaierror: 
        pass

