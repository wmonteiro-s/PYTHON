user_name = input("Digite seu nome de usuário: ")
while True:
    user_password = input("Digite sua senha: ")

    if len(user_password) <= 3:
        print("Senha inválida")
    else:
        break

d = {user_name: user_password}
print(d)