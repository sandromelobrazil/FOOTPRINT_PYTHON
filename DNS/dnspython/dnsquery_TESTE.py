
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 4 - dns_mx.py
# Looking up a mail domain - the part of an email address after the `@`

import sys
import dns

request = dns.request()

reply = request.req(name=uol.com.br, qtype=DNS.Type.A)
if reply.answers:
    for answer in reply.answers:
        print(istr, 'Hostname', hostname, '= A', answer['data'])

reply = request.req(name=uol.com.br, qtype=DNS.Type.AAAA)

if reply.answers:
    for answer in reply.answers:
        print(istr, 'Hostname', hostname, '= AAAA', answer['data'])

reply = request.req(name=uol.com.br, qtype=DNS.Type.CNAME)

if reply.answers:
    cname = reply.answers[0]['data']
    print(istr, 'Hostname', hostname, 'is an alias for', cname)
    resolve_hostname(cname, indent)

    
#dns.discovernameservers()
#resolve_email_domain(uol.com.br)


