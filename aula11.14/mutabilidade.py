# Alguns cuidados com dados mutáveis
# mutáveis - são dados que podem ter seu valor alterado na memória do dispositivo
# imutáveis - são dados que só podem ser copiados da memória do dispositivo
# copy - cria um novo endereço de memória

lista = ['João', 'Paulo']
lista[1] = 'Jose'
print(lista)
nome = 'Paulo'
#nome = 'João'
#nome[2] = 'a'
novo_nome = nome
nome = 'João'
print(nome)
print(novo_nome)

lista_a = ['João', 'Paulo']
print(lista_a)
lista_b = lista_a.copy()
lista_c = lista_b
lista_b[1] = 'Jose'
print(lista_a)
print(lista_b)
print(lista_c)