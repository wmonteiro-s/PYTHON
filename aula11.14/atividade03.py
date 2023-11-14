aluno1_nota1 = float(input("Digite uma nota para o aluno1: "))
aluno1_nota2 = float(input("Digite uma nota para o aluno1: "))
aluno1_nota3 = float(input("Digite uma nota para o aluno1: "))

aluno2_nota1 = float(input("\nDigite uma nota para o aluno2: "))
aluno2_nota2 = float(input("Digite uma nota para o aluno2: "))
aluno2_nota3 = float(input("Digite uma nota para o aluno2: "))

aluno3_nota1 = float(input("\nDigite uma nota para o aluno3: "))
aluno3_nota2 = float(input("Digite uma nota para o aluno3: "))
aluno3_nota3 = float(input("Digite uma nota para o aluno3: "))

aluno4_nota1 = float(input("\nDigite uma nota para o aluno4: "))
aluno4_nota2 = float(input("Digite uma nota para o aluno4: "))
aluno4_nota3 = float(input("Digite uma nota para o aluno4: "))

media_aluno1 = (aluno1_nota1 + aluno1_nota2 + aluno1_nota3) / 3
media_aluno2 = (aluno2_nota1 + aluno2_nota2 + aluno2_nota3) / 3
media_aluno3 = (aluno3_nota1 + aluno3_nota2 + aluno3_nota3) / 3
media_aluno4 = (aluno4_nota1 + aluno4_nota2 + aluno4_nota3) / 3

listamedia = [media_aluno1, media_aluno2, media_aluno3, media_aluno4]
print(f'As médias foram respectivamente {listamedia}')