# Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante, calcule e exibe a gorjeta do
# garçom, conderando 12% do valor da conta

def gorjeta(valor_conta):
    valor_conta = valor_conta * 0.12
    return valor_conta

print(gorjeta(100))