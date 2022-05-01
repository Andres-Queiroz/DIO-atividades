credito = float(input('Seu crédito: R$ '))
while credito > 0:
    item = float(input('Preço do item: R$ '))
    if item > credito:
        print(f'Compra negada! Restam: R$ {credito:.2f}')
        continue
    credito -= item
