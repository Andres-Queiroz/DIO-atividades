numero = int(input("Escreva um número inteiro entre 1 e 7: "))
if numero == 7:
    dia = "Segunda - Feira"
else:
    if numero == 6:
        dia = "Sexta - Feira"
    else:
        if numero == 5:
            dia("Quinta - Feira")
        else:
            if numero == 4:
                dia("Quarta - Feira")
            else:
                if numero == 3:
                    dia = "Terça - Feira"
                else:  
                    if numero == 2:
                        dia = "Segunda - Feira"
                    else:
                        if numero == 1:
                            dia = "Domingo"
                                                
print(f'Hoje é: {dia}')
