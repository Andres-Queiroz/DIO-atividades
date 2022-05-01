PN = float(input('Preço normal: '))
PP = float(input('Preço promoção: '))

f = (PP*100)/PN
g = 100-f

if g > 50:
    print('Dinheiro, na última sexta-feira de Novembro)')
elif g >30 and g < 49.99:
    print('Dinheiro')
elif g > 20 and g < 29.99:
    print('Crédito à vista')
elif g <20:
    print('Crédito parcelado')
