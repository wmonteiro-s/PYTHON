# Listas são um conjunto de elementos

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

# o sinal de "+" soma números e concatena strings
# extend - ele extende uma lista com outra, é como uma outra forma de concatenar listas com listas

a = 2
b = 3
print(a + b)

c = "Amo"
d = "Valley"
print(c + d)

lista_c = lista_a + lista_b
print(lista_c, type(lista_c))

lista_a.extend(lista_b)
print(lista_a)