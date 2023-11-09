nome = "Wesley"
altura = 1.80
peso = 75.80
imc = peso / altura * altura

print (nome, "tem", altura, "de altura,")
print("pesa", peso, "quilos e seu IMC é: ")
print(imc)

print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é: ')
print(f'{imc:.2f}')