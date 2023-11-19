# peça três temperaturas coloque em uma lista
# caso seja igual ou maior que 38 graus avisar que está com febre
# adicione duas novas temperaturas
# delete a temperatura do segundo indice
# delete a ULTIMA temperatura
# imprima os resultados

temperatura1 = float(input("Temperatura: "))
temperatura2 = float(input("Temperatura: "))
temperatura3 = float(input("Temperatura: "))

lista_temp = [temperatura1, temperatura2, temperatura3]

if(temperatura1 >= 38):
    print("Você está com febre")
if(temperatura2 >= 38):
    print("Você está com febre")
if(temperatura3 >= 38):
    print("Você está com febre")

lista_temp.append(float(input("Nova temperatura: ")))
lista_temp.append(float(input("Nova temperatura: ")))
del lista_temp[1]
del lista_temp[-1]
print(lista_temp)