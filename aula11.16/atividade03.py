# com meus_nomes = ['Ricardo', 'Roberto', 'Soares', 'Rivaldo', 'Richard', 'Andre']
# imprima na tela uma lista só com os nomes que não começam com 'R'
# remova os nomes dos indices impares

meus_nomes = ['Ricardo', 'Roberto', 'Soares', 'Rivaldo', 'Richard', 'Andre']

lista_sem_r = [meus_nomes[2], meus_nomes[5]]
print(lista_sem_r)

del meus_nomes[0::2]
print(meus_nomes)