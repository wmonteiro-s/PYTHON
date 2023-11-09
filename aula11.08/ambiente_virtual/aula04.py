# outra forma de interpolar

nome = "Geisa"
salario = 4500.99

print(nome, "ganha um salário de R$", salario)
print(f'O salário de {nome} é R$ {salario}')

# forma FORMAT de imprimir
# s - string
# d, i - int
# f - float
# x , X - hexa decimais
print('Quem ganha um salário de R$ %.2f é a %s   '% (salario,nome))