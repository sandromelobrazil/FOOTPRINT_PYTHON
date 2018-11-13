import dns.resolver
myquery = dns.resolver.Resolver()
target="kiku.com" 
answers = myquery.query(target, 'A')

for hostns in answers:
    print(hostns)
