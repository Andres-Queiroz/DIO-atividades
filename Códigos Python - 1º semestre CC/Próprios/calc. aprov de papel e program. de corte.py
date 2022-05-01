largura_formato_inteiro = int(input("largura em milímetros: "))
comprimento_formato_inteiro = int(input("comprimento em milímetros: "))
largura_formato_final = int(input("largura final em milímetros: "))
comprimento_formato_final = int(input("comprimento final em milímetros: "))
maior_maior = (largura_formato_inteiro // largura_formato_final)
menor_menor = (comprimento_formato_inteiro // comprimento_formato_final)
menor_maior = (largura_formato_inteiro // comprimento_formato_final)
maior_menor = (comprimento_formato_inteiro // largura_formato_final)
Paisagem = maior_maior * menor_menor
Retrato = menor_maior * maior_menor
print ("Paisagem = ", Paisagem)
print ("Retrato = ", Retrato)
print("True quer dizer que Paisagem é a melhor opção", Paisagem >=Retrato)


