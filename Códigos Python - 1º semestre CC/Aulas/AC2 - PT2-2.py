def encontrar_posicao(matriz,n):
  Lpos = []
  m = matriz[0][0]
  nlinhas = len(matriz)
  ncolunas = len(matriz[0])
  for lin in range(nlinhas):
    for col in range(ncolunas):
      if matriz[lin][col] == n:
          x = lin,col
          Lpos.append(x)
  return Lpos

#programa

matriz = ([2,1,0],[1,9,7],[9,2,1])
n = 1
print(encontrar_posicao(matriz,n))
