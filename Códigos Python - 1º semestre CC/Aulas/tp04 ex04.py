def maior(matriz):
    '''
    A função serve para encontrar
    o maior valor dentro da matriz quadrada.
    Matriz quadrada (2x2, 3x3, 4x4...).
    '''
    b = []  
    for i in range(len(matriz)):
        a = max(matriz[i])
        b.append(a)
        
    return max(b)


matriz = ([1,2,9],[4,10,6],[7,11,3])
print(maior(matriz))
