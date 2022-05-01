total = int(input())
mensal = int(input())
cont = 0

while total > 0:
    total = total - mensal
    cont += 1
    
    print(f'pagamento: {cont}')
    print(f'antes = {total + mensal}')
    if total < 0:
        total = 0
    print(f'depois = {total}')
    print('-----')
