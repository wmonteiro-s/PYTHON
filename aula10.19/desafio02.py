# variável altura recebe um input de tipo float que por sua vez recebe um valor de acordo com o usuário
height = float(input('Informe sua altura: '))

# função print para mostrar a mensagem e valores na tela
print(f'Se vc é um homem, seu peso ideal é: {(72.7 * height) - 58}')
print(f'Se vc é uma mulher, seu peso ideal é: {(62.1 * height) - 44.7}')
# vale ressaltar que o cálculo interpolado e o valor a ser mostrado é diferente de acordo com o gênero