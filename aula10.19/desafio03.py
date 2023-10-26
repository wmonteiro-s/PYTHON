# variável salário recebe um input de tipo float que por sua vez recebe um valor de acordo com o usuário 
wage = float(input('Digite o valor do seu salário: '))

# o mesmo acontece com a variável percentual_reajuste
percentage_adjustment = float(input('Digite o percentual de reajuste que queira aplicar em seu salário: '))

# função print para mostrar a mensagem e valores na tela
print(f'Seu antigo salário era {wage}, já seu atual salário após o reajuste é {((percentage_adjustment / 100) * wage) + wage}')
# vale ressaltar o cálculo interpolado na função que tem o intuito de mostrar o salário após o reajuste