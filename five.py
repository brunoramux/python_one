nome = input("Informe seu nome: ")
idade = int(input("Qual sua idade: "))

if idade >= 18:
    print("{} é maior de 18 e tem {} Anos".format(nome, idade))
else:
    print("{} é menor de 18 e tem {} Anos".format(nome, idade))