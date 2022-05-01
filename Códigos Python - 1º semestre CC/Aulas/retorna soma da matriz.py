def somadamatriz(M):
    s=0 #variavel acumuladora para calcular soma
    nlinhas = len(M)
    ncolunas = len(M[0])
    for lin in range(nlinhas):
        for col in range(ncolunas):
            s=s+M[lin][col]
    return s

M=[[0,1,2],[3,4,5],[6,7,8]]
print(somadamatriz(M))
