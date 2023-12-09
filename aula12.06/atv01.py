# lista = ['Josué', 10], ['Jeremias', 7.5], ['José', 5]
# print(lista)
# dic = {}
# dic.update(lista)
# print(dic)

# dic.update({'Jô': 9.5, 'Júlio': 4.5, 'João': 3, 'Juliana': 0})
# print(dic)

# lista = []
# marca = input("Digite a marca do carro: ")
# modelo = input("Digite o modelo do carro: ")

# lista.append(marca)
# lista.append(modelo)
# dic1 = {}
# dic1.update([lista])
# print(lista)
# print(dic1)

# cliente_nome = input("Digite seu nome: ")
# cliente_idade = int(input("Digite sua idade: "))
# cliente_aniversario = input("Digite sua data de aniversário: ")
# cliente_endereco = input("Digite seu endereço completo(rua, numero da residencia e bairro): ")

# dic2 = {}

# dic2.update({'cliente_nome':cliente_nome, 'cliente_idade':cliente_idade, 'cliente_aniversario':cliente_aniversario, 'cliente_endereco':cliente_endereco})
# print(dic2)

dic3 = {
    'wesley':'2684',
    'sedex':'0000'
}

user_name = input("Digite seu nome de usuário: ")
user_senha = input("Digite sua senha: ")

for chave, valor in dic3.items():
    if user_name == chave and user_senha == valor:
        print("Bem vindo")
    else:
        print("Acesso negado")
        
# if user_name in dic3.keys() and user_senha in dic3.values():
#     print("Bem vindo")
# else:
#     print("Acesso negado")

# dic_acesso = {
#     'alguem': '0123',
#     'outro:': '9999'
# }

# usuario_senha = {}
# usuario = input("Informe seu USUÁRIO: ")
# senha = input("Informe sua SENHA: ")

# usuario_senha[usuario]=senha

# for chave in dic_acesso.keys():
#     if chave == usuario:
#         if dic_acesso[chave] == usuario_senha[usuario]:
#             print(f'Bem vindo {usuario}')

# faz um quiz utilizando um dicionário com as seguintes chaves: Pergunta, opções e resposta. Faça a validação da opção 
# escolhida com a resposta e imprima

quiz = {
    "Pergunta 1": {
        "opções": ["a) opção A", "b) opção B", "c) opção C"],
        "resposta": "a"
    },
    "Pergunta 2": {
        "opções": ["a) opção A", "b) opção B", "c) opção C"],
        "resposta": "c"
    },
    "Pergunta 3": {
        "opções": ["a) opção A", "b) opção B", "c) opção C"],
        "resposta": "b"
    }
}

for pergunta, opcoes_resposta in quiz.items():
    print(pergunta)
    for opcao in opcoes_resposta["opções"]:
        print(opcao)
    resposta = input("Digite a letra da opção correta: ")
    if resposta == opcoes_resposta["resposta"]:
        print("Parabéns! Você acertou.")
    else:
        print("Que pena! Você errou.") 