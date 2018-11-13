import dns.resolver

target="kiku.com" 
answers = dns.resolver.query(target, 'A')

for hostA in answers:
    print(hostA)
