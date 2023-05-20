temp = []
menor = 0.0
soma = 0.0
media = 0.0
soma_media = 0
qtd_negativas = 0
qtd_positivas = 0

for i in range(0, 5):
   temp.insert(i, float(input("Digite a temperatua numero: " + str(i+1) + " ")))
   if i == 0:
       menor = temp[i]
   elif temp[i] < menor:
       menor = temp[i]
   if temp[i] > 0 and temp[i] < 20:
       soma += temp[i]
       soma_media += 1
   if temp[i] < 0:
       qtd_negativas += 1
   else:
       qtd_positivas += 1
       
media = soma / soma_media
   
print("{}".format(temp))
print("A menor temperatura e " + str(menor))
print("A media das temperaturas entre 0 e 20 e " + str(media))
print("Sao {} temperaturas negativas e {} positivas".format(qtd_negativas,qtd_positivas))

