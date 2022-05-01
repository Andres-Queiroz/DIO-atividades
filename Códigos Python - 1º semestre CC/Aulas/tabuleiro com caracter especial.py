def tabuleiro_diferente(a,b,c= str(object='')):
    linha = 0
    while linha < a:
        coluna = 0
        while coluna < b:
            print(c, end = "")
            coluna += 1
        print()
        linha += 1
