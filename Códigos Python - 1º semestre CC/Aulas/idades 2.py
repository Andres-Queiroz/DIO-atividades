idades = 1
soma = 0
i = 0

while idades >= 0:
    idades = int(input())
    if idades >= 0:
        i += 1
        soma = soma + idades
media = soma / i

print('{:.2f}'.format (media))
    
