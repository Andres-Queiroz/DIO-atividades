def tautograma(frase):
  frase  = frase.upper()
  x = frase.split()
  w = 0
  for i in range (len(x)):
    if x[i][0] == x[0][0]:
      w = w+1
  if w == len(x):
    return("Y")
  else:
    return('N')

#programa
frase = input()
print(tautograma(frase))
