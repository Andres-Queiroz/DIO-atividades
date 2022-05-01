nota = float(input('Qual a nota? ')) #1

if nota >= 9: #2
    letra = 'A' #3
else:
    if nota >= 8: #4
        letra = 'B' #5
    else:
	    if nota >= 6: #6
		letra = 'C' #7
	    else:
		    if nota >= 4: #8
			letra = 'D' #9
		    else:
                        letra = 'E' #10
                        
print(f'Sua letra é: {letra}') #11
