tupla = (10,30,40,20,40,30,33,55,66,33,2,1,4,5,6,7,66,77,121,23,43,65,7,
         8,10,21,34,54,66,447,86,432,65,45,23,12,32,456,65,3,12)

maximo = 0
max = 0
valor = False
for a in tupla:
  maximo = tupla.count(a)
  if maximo > max:
    max = maximo
    valor = a
print('valor',valor, 'qtd:',max)
