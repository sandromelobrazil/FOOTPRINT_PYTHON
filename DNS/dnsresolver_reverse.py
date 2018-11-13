import dns.reversename
target="1.1.1.1" 

answers = dns.reversename.from_address(target)
answers2 = dns.reversename.to_address(answers)

print("Resultado da consulta reversa do IP " + target + " eh -> " + str(answers))
print("Resultado da consulta reversa do IP " + target + " eh -> " + str(answers2))



