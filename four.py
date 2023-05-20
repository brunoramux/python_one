qtd_meses = int(input("Por quantos meses deseja fazer controle alimentar: "))
kilos = float(input("Quantos quilos deseja perder: "))
qtd_mes = kilos / qtd_meses

for i in range(0, qtd_meses):
    print("Mes {} voce ira perder {}KG".format(i+1, qtd_mes))