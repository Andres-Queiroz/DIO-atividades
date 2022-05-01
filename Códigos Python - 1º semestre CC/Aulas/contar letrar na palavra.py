def contarletras(s,letra):
    c=0
    for x in s:
        if x == letra:
            c=c+1
    return c

palavra1 = "PARALELEPIPEDO"
print('O numero de letras P em ', palavra1, 'é', contarletras(palavra1, 'P'))
print('O numero de letras A em ', palavra1, 'é',contarletras(palavra1, 'A'))
print('O numero de letras R em ', palavra1, 'é',contarletras(palavra1, 'R'))
print('O numero de letras L em ', palavra1, 'é',contarletras(palavra1, 'L'))
print('O numero de letras E em ', palavra1, 'é',contarletras(palavra1, 'E'))
print('O numero de letras I em ', palavra1, 'é',contarletras(palavra1, 'I'))
print('O numero de letras O em ', palavra1, 'é',contarletras(palavra1, 'O'))
