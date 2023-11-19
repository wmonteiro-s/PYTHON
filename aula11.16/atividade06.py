# peça cinco nomes e coloque os nomes em uma lista
# Se o nome iniciar com Consoante avise "Seu nome inicia com Consoante"
# adicone um nome no inicio da lista e imprima a lista

nome1 = input("Digite um nome: ")
nome2 = input("Digite um nome: ")
nome3 = input("Digite um nome: ")
nome4 = input("Digite um nome: ")
nome5 = input("Digite um nome: ")

lista = [nome1, nome2, nome3, nome4, nome5]
print(lista,"\n")

if nome1[0] != "a" and nome1[0] != "e" and nome1[0] != "i" and nome1[0] != "o" and nome1[0] != "u" \
and nome1[0] != "A" and nome1[0] != "E" and nome1[0] != "I" and nome1[0] != "O" and nome1[0] != "U" \
and nome1[0] != "0" and nome1[0] != "1" and nome1[0] != "2" and nome1[0] != "3" and nome1[0] != "4" \
and nome1[0] != "5" and nome1[0] != "6" and nome1[0] != "7" and nome1[0] != "8" and nome1[0] != "9":
    print(f'O nome {nome1} começa com uma consoante')
else:
    print(f'O nome {nome1} não começa com uma consoante')

if nome2[0] != "a" and nome2[0] != "e" and nome2[0] != "i" and nome2[0] != "o" and nome2[0] != "u" \
and nome2[0] != "A" and nome2[0] != "E" and nome2[0] != "I" and nome2[0] != "O" and nome2[0] != "U" \
and nome2[0] != "0" and nome2[0] != "1" and nome2[0] != "2" and nome2[0] != "3" and nome2[0] != "4" \
and nome2[0] != "5" and nome2[0] != "6" and nome2[0] != "7" and nome2[0] != "8" and nome2[0] != "9":
    print(f'O nome {nome2} começa com uma consoante')
else:
    print(f'O nome {nome2} não começa com uma consoante')

if nome3[0] != "a" and nome3[0] != "e" and nome3[0] != "i" and nome3[0] != "o" and nome3[0] != "u" \
and nome3[0] != "A" and nome3[0] != "E" and nome3[0] != "I" and nome3[0] != "O" and nome3[0] != "U" \
and nome3[0] != "0" and nome3[0] != "1" and nome3[0] != "2" and nome3[0] != "3" and nome3[0] != "4" \
and nome3[0] != "5" and nome3[0] != "6" and nome3[0] != "7" and nome3[0] != "8" and nome3[0] != "9":
    print(f'O nome {nome3} começa com uma consoante')
else:
    print(f'O nome {nome3} não começa uma consoante')

if nome4[0] != "a" and nome4[0] != "e" and nome4[0] != "i" and nome4[0] != "o" and nome4[0] != "u" \
and nome4[0] != "A" and nome4[0] != "E" and nome4[0] != "I" and nome4[0] != "O" and nome4[0] != "U" \
and nome4[0] != "0" and nome4[0] != "1" and nome4[0] != "2" and nome4[0] != "3" and nome4[0] != "4" \
and nome4[0] != "5" and nome4[0] != "6" and nome4[0] != "7" and nome4[0] != "8" and nome4[0] != "9":
    print(f'O nome {nome4} começa com uma consoante')
else:
    print(f'O nome {nome4} não começa com uma consoante')

if nome5[0] != "a" and nome5[0] != "e" and nome5[0] != "i" and nome5[0] != "o" and nome5[0] != "u" \
and nome5[0] != "A" and nome5[0] != "E" and nome5[0] != "I" and nome5[0] != "O" and nome5[0] != "U" \
and nome5[0] != "0" and nome5[0] != "1" and nome5[0] != "2" and nome5[0] != "3" and nome5[0] != "4" \
and nome5[0] != "5" and nome5[0] != "6" and nome5[0] != "7" and nome5[0] != "8" and nome5[0] != "9":
    print(f'O nome {nome5} começa com uma consoante')
else:
    print(f'O nome {nome5} não começa com uma consoante')

lista.insert(0, input("\nDigite um novo nome: "))
print(lista)