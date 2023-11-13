# uma lista é representada pelos "[]" colchetes
# len - metodo que retorna a quantidade de itens de uma lista
# append metodo que insere itens no final da lista
# del - remove item especifico da lista pelo seu indice
# remove - remove item pelo objeto (seu valor)
# pop - remove o último objeto da lista
# insert - adiciona um objeto num determinado local 
#obs: todo metodo por obrigação retorna algum valor

'''lista = []
print(lista, type(lista))
print(len(lista))

lista = ['front']
print(lista, type(lista))
print(len(lista))

lista = ['back']
print(lista, type(lista))
print(len(lista))

lista.append('front')
print(lista, type(lista))
print(len(lista))'''

#           0       1      2    3     4
# REVERSE   -5      -4     -3   -2    -1
lista = [ 'back', 'tarde', 21, True, 8.8]
print(f'A quantidade de alunos na turma é {lista[2]}')
lista[2] = 22
print(lista)
lista[1] = False
print(lista)
lista[1] = ['Neyva', 'Alice', 'Lara', 'Paula', 'Geisa']
print(lista[1][2])

print(lista)
del lista[-2]
print(lista)
del lista[-2]
print(lista)
del lista[-2]
print(lista)

lista.remove('back')
print(lista)

lista.append(26)
lista.append(57)
lista.append(900)
print(lista)

valor_do_pop = lista.pop()
print(lista)

print(f'Foi removido da lista o cliente de Id: {valor_do_pop}')

lista.insert(0, 'Amontada Valley')
print(lista)
lista.insert(2, 'Professor')
print(lista)
lista.insert(200, 'aluna')
print(lista)