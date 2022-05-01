def maiorpar(lista):
    maior = 0      #para guardar o maior numero 
    elementos = len(lista) #conta quantos elementos há na lista
    for i in range(elementos):
        if lista[i] % 2 == 0: #se o resto da divisão do elemento for 0
            par = lista[i]   # o numero sera par
            if par > maior:         #se o numero par for maior que o armazenado
                maior = par       #o numero resultante da divisão for maior que o que esta guardado no par, susbtituirá-o
    print (maior)

lista = [1,5,22,36,15,44,12,88,76,75,70,95,100]
print(maiorpar(lista))
