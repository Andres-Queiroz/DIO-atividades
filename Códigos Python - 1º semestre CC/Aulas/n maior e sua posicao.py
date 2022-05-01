n = int(input())
cont = 0

for i in range (1, 100):
    a = int(input())
    if a > cont:
        maior = a
        posicao = i + 1
        cont = a

print(maior)
print(posicao)
