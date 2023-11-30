# Faça um programa, com uma função que necessite de um argumento. A função retorna 'P', se seu argumento for positivo, 
# e 'N' se for, se seu argumento for zero ou negativo

def funcao(arg):
    if arg > 0:
        return("P")
    elif arg <= 0:
        return("N")

print(funcao(0))