def converter(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

def exibir(lista_de_codigos):
    for i in range(len(lista_de_codigos)):
        if i < len(lista_de_codigos) -1:
            print(lista_de_codigos[i], end=' ')
        else:
            print(lista_de_codigos[i])

lista_de_codigos = input().split()
if lista_de_codigos != []:
    converter(lista_de_codigos)

comandos = input().split()

while comandos[0] != 'encerrar':
    if comandos[0] == 'adicionar':
        lista_de_codigos.append(int(comandos[1]))
    elif comandos [0] == 'remover':
        comandos[1] = int(comandos[1])
        if comandos [1] in lista_de_codigos:
             lista_de_codigos.remove(comandos[1])
        else:
             print(f'código {comandos[1]} não encontrado')
    else:
        lista_de_codigos.sort()       
        exibir(lista_de_codigos)  
    comandos = input().split() 
lista_de_codigos.sort()       
exibir(lista_de_codigos)
