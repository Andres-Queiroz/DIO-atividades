def tabuleiro(x,y):
    linha = 0
    while linha < x:
        coluna = 0
        while coluna < y:
            if (linha+coluna) % 2 == 0:
                print(2 * chr(9608), end='')
            else:
                print(2 * " " , end='')
            coluna += 1
        print()
        linha += 1
