def procura(M,N):
    s=0 #variavel acumuladora para calcular soma
    X = []

    nlinhas = len(M)
    ncolunas = len(M[0])
    for lin in range(nlinhas):
        for col in range(ncolunas):
            if M[lin][col] > N:
                X.append(M[lin][col])
    return X

M=[[0,1,2],[3,4,5],[6,7,8]]
print(procura(M,6))

