idade = int(input('Qual a sua idade? '))
cnh = input('Você tem CNH? (s/n)')
maior_de_idade = idade >= 18
possui_cnh = cnh == 's'
pode_dirigir = maior_de_idade and possui_cnh
if pode_dirigir:
    print('Você pode dirigir.')
