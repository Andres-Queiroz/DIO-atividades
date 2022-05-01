lista= []

x = int(input())
soma = 0
cont = 0
z = 0
while x > 0:
    soma += x
    cont += 1
    media = soma / cont
    lista.append(x)
    x = int(input())
    z += 1
print('MEDIA: %.2f' %media)

for i in range(0, z):
    if (lista[i]) < media:
        print(lista[i])
