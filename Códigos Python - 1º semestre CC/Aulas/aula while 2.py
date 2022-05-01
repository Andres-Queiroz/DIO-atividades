a = input('Digite uma letra minúscula: ')
contador = 0
while a != 'x':
    contador += 1
    a = input('tente novamente: ')
print(f'Quantidade de tentativas: {contador} vezes')
