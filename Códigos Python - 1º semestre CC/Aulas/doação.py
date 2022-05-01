a = 0
vic = 2.50
cont = 0
while a >= 0:
    cont = cont + a
    valor = cont * vic
    a = float(input())
    
print('VC$ %.2f'%cont)
print('R$ %.2f'%valor)
