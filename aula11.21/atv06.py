# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado
# de temperaturas em graus celsius, e informe ao final a menor e a maior temperaturas informadas. Para sair do 
# programa deve digitar "SAIR"

# maior = 0
# menor = None

# while True:
#     saida = input("Para sair do programa digite 'SAIR': ")
#     if saida == "SAIR" or saida == "sair":
#         break
#     temp = float(input("Digite a temperatura: "))
#     if temp > maior:
#         maior = temp
#     if temp == None or temp < menor:
#         menor = temp

# print(f'A menor temperatura é {menor} e a maior é {maior}')

lista = []
while True:
    saida = input("Para sair do programa digite 'SAIR': ")
    if saida == "SAIR" or saida == "sair":
        break
    temp = float(input("Digite a temperatura: "))
    lista.append(temp)

    
print(lista)
print(f'A menor temperatura é {min(lista)} e a maior é {max(lista)}')