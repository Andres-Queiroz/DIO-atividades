numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

while True:
    a = int(input('digite o numero '))
    if 0 <= a <=20:
        break
print(f'voce digitou o numero {numeros[a]}')
