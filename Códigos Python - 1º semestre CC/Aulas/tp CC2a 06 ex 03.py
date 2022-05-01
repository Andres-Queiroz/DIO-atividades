def somadiagonalp(M):
    s=0 #variavel acumuladora para calcular soma
    nlinhas = len(M)
    ncolunas = len(M[0])
    for lin in range(nlinhas):
        for col in range(ncolunas):
            if lin == col:
                s=s+M[lin][col]
    if s % 2 == 0:
        return(True)
    else:
        return(False)

M1=[[1,2,3],[4,5,6],[7,8,9]]
M2=[[1,2,3],[4,6,6],[7,8,9]]
M3=[[12,17,32],[42,61,63],[17,18,9]]

print(somadiagonalp(M1))
print(somadiagonalp(M2))
print(somadiagonalp(M3))

#outra solução
def soomaD(M):
    s=0 #variavel acumuladora para soma
    nlinhas = len(M)
    for lin in range(nlinhas):
        s = s+M[lin][lin]
    return s%2 == 0


M1=[[1,2,3],[4,5,6],[7,8,9]]
M2=[[1,2,3],[4,6,6],[7,8,9]]
M3=[[12,17,32],[42,61,63],[17,18,9]]

print(soomaD(M1))
print(soomaD(M2))
print(soomaD(M3))
