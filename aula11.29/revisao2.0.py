# estruturas condicionais
variavel = 120
if variavel < 20:
    print("Menor que 20")
elif variavel == 20:
    print("Igual a 20")
elif variavel > 20 and variavel < 50:
    print("Está no intervalo entre 21 e 49")
else:
    print("Qualquer outra coisa")

# estruturas de repetição
# for e while

# Fazer 10 questões em um codigo e dizer se esta correto ou errado
q1 = "V"
q2 = "F"
q3 = "V"
q4 = "F"
q5 = "V"
q6 = "F"
q7 = "V"
q8 = "F"
q9 = "V"
q10 = "F"
questoes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
for questao in questoes:
    questoes = input('A questão é verdadeira[V] ou falsa[F]? ')
    if questoes.lower() == questao.lower():
        print('Você acertou!')
    elif questoes.lower() != questao.lower():
        print('Você errou.')