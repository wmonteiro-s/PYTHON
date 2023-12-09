# CRUD - Created, Readed, Updated, Deleted

dic = {'nome' : 'Wesley'} #created
dic2 = dict(idade = 18) #created

dic['nome'] # readed
dic2.get('idade') # readed

dic.update(sobrenome = 'Monteiro') #updated
dic.update({'idade' : '18'}) #updated
#para adicionar iteráveis no dicionário é preciso uma vígula no fim
tupla = ('peso', 72.12), #updated
lista = ['data', '28/01/2005'], ['numeros',[1,2,3,4,5,6,7,8,9]] #updated
dic.update(tupla)
dic.update(lista)

dic.clear() #deleted


print(f'Dados do dicionário: {dic}')
print(dic2)