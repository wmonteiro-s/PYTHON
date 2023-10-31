km = float(input("Quantos quilômetros foram percorridos? "))
litros = float(input("Quantos litros de combustível foram gastos? "))

consumo_por_km = km / litros

if consumo_por_km < 8.0:
    print("Venda o carro")
elif consumo_por_km > 8.0 and consumo_por_km < 14.0:
    print("Econômico")
elif consumo_por_km > 14.0:
    print("Super econômico")
else:
    print("Inválido")