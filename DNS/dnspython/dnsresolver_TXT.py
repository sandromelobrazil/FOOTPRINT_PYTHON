import dns.resolver

target="facebook.com" 
answers = dns.resolver.query(target, 'TXT')

for dnstxt in answers:
    print(dnstxt)
