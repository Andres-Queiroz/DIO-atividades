from random import randint

matriz = [[],[],[]]
def paresmaior(matriz, N):
    lista = []
    for y in range(len(matriz)):
        for x in range (len(matriz[y])):
            if matriz[y][x] % 2 == 0 and matriz[y][x] > N:
                lista.append(matriz[y][x])
    return lista

N = int(input())
while len(matriz[0]) < 3 and len(matriz[1]) < 3 and len(matriz[2]) < 3:
    a = randint(0,100)
    b = randint(0,100)
    c = randint(0,100)
    matriz[0].append(a)
    matriz[1].append(b)
    matriz[2].append(c)
print ('Vetor criado: ', matriz)

print('Elementos maior que',N,paresmaior(matriz, N))
print('Soma dos elementos pares maior que',N,'é:', sum(paresmaior(matriz, N)))
