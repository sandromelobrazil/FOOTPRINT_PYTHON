import dns.resolver

target="kiku.com" 
answers = dns.resolver.query(target, 'NS')

for hostns in answers:
    print(hostns)
