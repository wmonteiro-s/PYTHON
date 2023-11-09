# Fatiamento de strings
# OBS: toda string por padrão é um input que não saiu do armário
# ordem de tratamento
# 12345678........
# -87654321.......
# [i:f:p] = i - INICIO, f - FIM, p - PARSE

nome = "Wesley Monteiro de Sousa"
print(nome[17:23])
print(nome[-6:])
print(nome[0::2]) #par
print(nome[1::2]) #ímpar

lista_nome = ("W", "e", "s", "l", "e", "y")

print("=" * 20)
print(nome[3]) 
print(nome[-2])

print(lista_nome[3]) 
print(lista_nome[-2])