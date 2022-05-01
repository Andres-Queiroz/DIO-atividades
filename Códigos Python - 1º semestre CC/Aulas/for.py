salarios = [0, 0, 0, 0]
soma = 0
i = 0 # variável que será usada como índice.
while i < 4:
    salarios[i] = float(input('Salário: R$ '))
    soma += salarios[i]
    i += 1
media = soma / 4
i = 0 # variável que será usada como índice.
while i < 4:
    if salarios[i] < media:
        print(f'Abaixo da média: R$ {salarios[i]:.2f}')
    
    i += 1
