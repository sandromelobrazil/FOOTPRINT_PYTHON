import dns.resolver

answers = dns.resolver.query('dnspython.org', 'MX')
print(answers)

for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
