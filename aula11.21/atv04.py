# Faça um programa que peça para 10 pessoas a sua idade, ao final o programa devera verificar se
# a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, dizer se a turma
# é jovem ou adulta ou idosa, conforme a média calculada

soma_idade = 0
contador = 0
for i in range(10):
    idade = int(input("Digite a idade do aluno: "))
    soma_idade += idade
    contador += 1

media = soma_idade / contador
if media > 0 and media <= 25:
    print("A turma é jovem")
elif media > 25 and media <= 60:
    print("A turma é adulta")
else:
    print("A turma é adulta")
