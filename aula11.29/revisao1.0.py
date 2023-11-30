variavel = 1
print(variavel)

variavel = "wesley"
print(variavel)

# regra do fatiamento [inicio: fim: step]
print(variavel[-1:-7:-1])


#utilizando fatiamento e repetição imprima uma lista de "a" até "e" removendo uma letra de cada vez
lista = ["a", "b", "c", "d", "e"]
tamanho = len(lista)

for i in lista:
    print(lista[0:tamanho])
    tamanho -= 1

for i in range(5):
    print(lista[0:5-i])