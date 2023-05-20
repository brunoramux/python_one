
mes_atual = int(input("Digite o mes atual: "))
total = 0

for i in range (1,12):
    if i < mes_atual:
        total += i



print("A soma dos valores menores que o mes atual e igual a {}".format(total))
if mes_atual == 12:
    print ("O proximo mes e 1")
else:
    print("O proximo mes e {}".format(mes_atual + 1))

if mes_atual % 2 == 0:
    print("Mes atual e par!")
else:
    print("Mes atual e impar!")


