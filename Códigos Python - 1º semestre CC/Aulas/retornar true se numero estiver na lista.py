def existe(a):
    if a in lista:
        print(True)
    else:
        print(False)

a = int(input())
lista = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(existe(a))
