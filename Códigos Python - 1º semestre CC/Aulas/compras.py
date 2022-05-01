a = float(input("Digite o credito disponivel "))
credito = a
total = 0
contador = 1
preco = float(input("Digite o valor do item 1 "))
while preco <= credito:
    total +=preco
    credito -=preco
    contador += 1
    preco = float(input(f"Digite o valor do item {contador} "))
print(f'compra do item {contador} negada!')
print(f'Foi efetuada a compra de {contador - 1} itens')
print(f'Total da compra {total:.2f}')
print(f'Credito ainda disponivel {credito:.2f}')
