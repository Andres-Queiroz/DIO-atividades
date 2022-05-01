a = int(input('total de alunos: '))

lista = []
lista2 = []


for x in range (1,a+1):
    b = float(input())
    lista.append(b)
    x += 1
for z in range (1,a+1):
    c = float(input())
    lista2.append(c)
    z += 1
g = 0
for y in range (0,a):
    if lista[y] < 10 and lista2[y] == 10:
        g += 1
print('NOTAS ALTERADAS:', g)

cont = 00
while cont < a:
    if lista2[cont] == 10 :
        if lista[cont] < 8:
            print(f'*({cont+1:03}) original: 0{lista[cont]:.2f} | final: 0{lista[cont] + 2 :.2f}')
        elif lista[cont] == 8:
            print(f'*({cont+1:03}) original: 0{lista[cont]:.2f} | final: {lista[cont] + 2 :.2f}')
        elif lista[cont] == 9:
            print(f'*({cont+1:03}) original: 0{lista[cont]:.2f} | final: {lista[cont] + 1 :.2f}')
        elif lista[cont] == 10:
            print(f'-({cont+1:03}) original: {lista[cont]:.2f} | final: {lista[cont]:.2f}')
    elif lista2[cont] != 10:
        if lista[cont] == 10:
            print(f'-({cont+1:03}) original: {lista[cont]:.2f} | final: {lista[cont]:.2f}')
        elif lista[cont] < 10:
            print(f'-({cont+1:03}) original: 0{lista[cont]:.2f} | final: 0{lista[cont]:.2f}')
    cont += 1
