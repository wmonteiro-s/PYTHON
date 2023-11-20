while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    if senha == nome:
        print("ERRO!")
    else:
        print("Bem vindo!")
        break