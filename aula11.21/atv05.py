# Supondo que a população de um país A seja de 80000 habitantes com uma taxa anual de crescimento de 3% Faça um
# programa que calcule e escreva o número de anos necessários para que a população do país A chegar a 120000 habitantes

cresc_anual = 0.03
populacao_inicial, populacao_final = 80000, 120000
anos = 0

while populacao_inicial < populacao_final:
    anos += 1
    populacao_inicial = populacao_inicial + (populacao_inicial * cresc_anual)

if populacao_inicial >= populacao_final:
    print(f'A população do país A ultrapassará {populacao_final} habitantes em {anos} anos')