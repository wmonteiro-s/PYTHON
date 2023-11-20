contador = 0
maior = 0

while contador < 5:
    numero = int(input("Digite um número: "))
    
    if maior < numero:
        maior = numero

    contador += 1
print(maior)