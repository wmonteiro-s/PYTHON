# Set - conjuntos

set01 = set('Paulo')
set02 = {'Paulo', 'Junior', 'Lara', 'Junior', 'Kaynan', 'Junior', 'Felipe', 'Junior'}
print(set01)
print(set02)

lista = [1,2,3,4,5,5,5,5,5,5]
print(lista)
set03 = set(lista)
print(set03)

for i in set03:
  print(i)

set03.add('Paulo')
print(set03)

set03.update('João')
print(set03)

set03.discard('Paulo')
print(set03)

set03.clear()
print(set03)

set04 = {1, 2, 3, 4, 5}
set05 = {4, 5, 6, 7, 8}

set06 = set04  | set05 # União de conjuntos
print(set06)

set07 = set04 & set05 # Intercessão de conjuntos
print(set07)

set08 = set04 - set05 # Diferença entre conjuntos
print(set08)
set09 = set05 - set04 # Diferença entre conjuntos
print(set09)