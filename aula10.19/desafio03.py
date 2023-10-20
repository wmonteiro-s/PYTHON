# variável salário recebe um input de tipo float que por sua vez recebe um valor de acordo com o usuário 
salario = float(input('Digite o valor do seu salário: '))

# o mesmo acontece com a variável percentual_reajuste
percentual_reajuste = float(input('Digite o percentual de reajuste que queira aplicar em seu salário: '))

# função print para mostrar a mensagem e valores na tela
print(f'Seu antigo salário era {salario}, já seu atual salário após o reajuste é {((percentual_reajuste / 100) * salario) + salario}')
# vale ressaltar o cálculo interpolado na função que tem o intuito de mostrar o salário após o reajuste