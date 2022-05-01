def contaletras(S,letra):
    c=0
    v=[]
    for i in range(len(palavra)):
        if S[i]==letra:
            c=c+1
            v.append(i)
    return c

palavra = "PARALELEPIPEDO"
letra = 'P'
print('O numero de letras ', letra, 'em ', palavra, "é ", contaletras(palavra,letra))
