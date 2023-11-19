contador = 1

while contador <= 20:
    idade_alunos = int(input(f'Digite a idade do aluno {contador}: ')) 

    if idade_alunos > 13:
        print(f'O aluno {contador} tem mais de 13 anos')
    
    contador += 1