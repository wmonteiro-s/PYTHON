# variável f recebe um input de tipo float que por sua vez recebe um valor de acordo com o usuário
f = float(input('Qual a temperatura em graus Farenheit? '))

# função print para mostrar a mensagem e valores na tela
print(f'A temperatura convertida em graus Celsius é, {5 * (f - 32) / 9}')
# vale ressaltar o cálculo interpolado na função que tem o intuito de mostrar a temperatura convertida em graus Celsius