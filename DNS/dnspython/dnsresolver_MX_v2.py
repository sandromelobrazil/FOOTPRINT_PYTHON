import dns.resolver

target="kiku.com" 
answers = dns.resolver.query(target, 'MX')

for hostns in answers:
    print(hostns.exchange)
