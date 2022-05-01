qtd = int(input())
lista1 = [] #canais
lista2 = [] #inscritos
lista3 = [] #money
lista4 = [] #é premium ou não?
for i in range (1, qtd+1):
    canais_inscritos_money_premium = input()
    canais,inscritos,money,premium = canais_inscritos_money_premium.split(';')
    lista1.append(canais)
    lista2.append(inscritos)
    lista3.append(money)
    lista4.append(premium)

p = float(input()) #premium
n = float(input()) #normal

print('-----\nBÔNUS\n-----')

for j in range(0,qtd):
    if int(lista2[j]) >= 1000:
        formula = int(lista2[j]) // 1000
        if float(lista3[j]) < 1:
            print('{}: R$ {:.2f}'.format(lista1[j], formula))
        else:
            if lista4[j] == 'sim':
                formula2 = (formula * p) + float(lista3[j])
                print('{}: R$ {:.2f}'.format(lista1[j], formula2))
            elif lista4[j] == 'não':
                formula2 = (formula * n) + float(lista3[j])
                print('{}: R$ {:.2f}'.format(lista1[j], formula2))
    else:
        print('{}: R$ {:.2f}'.format(lista1[j], float(lista3[j])))



