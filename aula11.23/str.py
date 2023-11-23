# count - a função conta quantas vezes um determinado caractere aparece em uma string
# upper e lower - dois método que deixam a string toda em maiúsculo e minusculo
# find - busca por uma expressão dentro da frase
# capitalize - deixa a primeira letra maiúscula
# 

frase = "A Banana é amarela e o abacate é verde.".lower()
letra = "a"
email = " wmonteiro873@gmail.com "

print(f'A letra "{letra}" aparece {frase.count(letra)} vezes na frase "{frase}"')
saida = input("Digite 's' para sair: ").upper

if saida == 'S':
    print(saida)

achei = frase.find('roxo')
if achei >= 0:
    print(f'A expressão foi encontrado na frase no índice {achei}')
else:
    print('A expressão NÃO foi encontrado na frase')

nova_frase = frase.replace('banana', 'maracujá')
nova_frase2 = frase.replace('abacate', 'manga')
nova_frase2 = email.replace(' ', '')
print(frase)
print(nova_frase)
print(nova_frase2)
print(frase.capitalize())
print(frase.split())