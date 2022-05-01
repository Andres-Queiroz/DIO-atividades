lista = []
for i in range(1,101,1):
    lista.append(i)
p = []
v = []
#descobrir posições
for x in range (len(lista)):
    if lista[x] <= 10:
        p.append(x)
print('Posições dos valores menor que 10:', p)
#valores respectivos as posições
for y in range (len(p)):
    v.append(lista[p[y]])
print('Valores respectivos as posições:',v)

media = sum(v) / len(v)
print('Média dos valores menores que 10 é:',(media))
