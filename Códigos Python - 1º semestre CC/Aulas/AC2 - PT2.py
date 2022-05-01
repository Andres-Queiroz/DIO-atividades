matriz = ([7,1,2],[2,7,1],[2,4,6])
n = 7


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
  return  m, Lpos

print(encontrar_posicao(matriz,n))
