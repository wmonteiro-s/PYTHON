# peça cinco nomes e coloque os nomes em uma lista
# Se o nome iniciar com Vogal avise "Seu nome inicia com vogal"
# remova o nome do meio
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')
nome5 = input('Digite um nome: ')

lista = [nome1, nome2, nome3, nome4, nome5]
print(lista)

if nome1[0] == 'a' or nome1[0] == 'e' or nome1[0] == 'i' or nome1[0] == 'o' or nome1[0] == 'u' \
or nome1[0] == 'A' or nome1[0] == 'E' or nome1[0] == 'I' or nome1[0] == 'O' or nome1[0] == 'U':
    print(f'O nome {nome1} inicia com vogal')
else:
    print(f'O nome {nome1} não começa com vogal')

if nome2[0] == 'a' or nome2[0] == 'e' or nome2[0] == 'i' or nome2[0] == 'o' or nome2[0] == 'u' \
or nome2[0] == 'A' or nome2[0] == 'E' or nome2[0] == 'I' or nome2[0] == 'O' or nome2[0] == 'U':
    print(f'O nome {nome2} inicia com vogal')
else:
    print(f'O nome {nome2} não começa com vogal')

if nome3[0] == 'a' or nome3[0] == 'e' or nome3[0] == 'i' or nome3[0] == 'o' or nome3[0] == 'u' \
or nome3[0] == 'A' or nome3[0] == 'E' or nome3[0] == 'I' or nome3[0] == 'O' or nome3[0] == 'U':
    print(f'O nome {nome3} inicia com vogal')
else:
    print(f'O nome {nome3} não começa com vogal')


if nome4[0] == 'a' or nome4[0] == 'e' or nome4[0] == 'i' or nome4[0] == 'o' or nome4[0] == 'u' \
or nome4[0] == 'A' or nome4[0] == 'E' or nome4[0] == 'I' or nome4[0] == 'O' or nome4[0] == 'U':
    print(f'O nome {nome4} inicia com vogal')
else:
    print(f'O nome {nome4} não começa com vogal')

if nome5[0] == 'a' or nome5[0] == 'e' or nome5[0] == 'i' or nome5[0] == 'o' or nome5[0] == 'u' \
or nome5[0] == 'A' or nome5[0] == 'E' or nome5[0] == 'I' or nome5[0] == 'O' or nome5[0] == 'U':
    print(f'O nome {nome5} inicia com vogal')
else:
    print(f'O nome {nome5} não começa com vogal')

del lista[2]
print(lista)