a = int(input('Quantos salários serão inseridos?: '))
soma = 0

while a >= 0:
    salario = float(input('Salário: R$ '))
    soma += salario
    media = soma / a
    if a < 0:
        break
    if salario < media:
         print(f'Abaixo da média: R$ {salario:.2f}')
print ('fim')    
