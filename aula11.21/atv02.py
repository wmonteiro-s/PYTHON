# Faça um programa que dado um valor um conjunto de N números, determine o menor valor, o maior valor e
# e a soma dos valores

maior = 0
menor = None
while True:
    saida = input("Aperte 'S' para sair do loop e 'E' para continuar: ")
    if saida == "s" or saida == "S":
        break
    if saida == "e" or saida == "e":
        numero = int(input("Digite um número: "))
        if numero > maior:
            maior = numero
        if menor == None or numero < menor:
            menor = numero
    else:
        continue

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
print(f'{maior} + {menor} = {menor + maior}')