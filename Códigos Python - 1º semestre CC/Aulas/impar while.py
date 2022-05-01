a = int(input())
b = int(input())

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
soma = 0
contador = menor + 1

while contador < maior:
    if contador % 2 == 1:
        soma += contador
    contador += 1
print("%d" %soma)
