#formato inteiro em milímetros
largura1 = int(input("Largura do formato inteiro: "))
comprimento1 = int(input("Comprimento do formato inteiro: "))
#formato final em milímetros
largura2 = int(input("Largura do formato final: "))
comprimento2 = int(input("Comprimento do formato final: "))
#1º passo transformar em metros
largura1_metros = largura1/1000
comprimento1_metros = comprimento1/1000

largura2_metros = largura2/1000
comprimento2_metros = comprimento2/1000

#2º passo aprov (P ou R)
menor_menor = largura1 // largura2
maior_maior = comprimento1 // comprimento2
menor_maior = largura1 // comprimento2
maior_menor = comprimento1 // largura2

#3º passo Paisagem ou retrato
Paisagem = (menor_menor * maior_maior)
Retrato = (menor_maior * maior_menor)
print("Paisagem = ", Paisagem, "Retrato = ", Retrato)

#4º passo área folha inteira em metros
area0 = largura1_metros * comprimento1_metros
area1 = ((menor_menor * largura2)/1000) * ((maior_maior * comprimento2)/1000)
area2 = ((menor_maior * comprimento2)/1000) * ((maior_menor * largura2)/1000)

#5ºpasso parte/todo
porcentagem_aprov = (area1 / area0)*100
porcentagem_perda = 100-porcentagem_aprov
print("Porcentagem de aproveitamento Paisagem: %.2f" %porcentagem_aprov, "%")
print("Porcentagem de perda Paisagem: %.2f" %porcentagem_perda, "%")

porcentagem_aprov = (area2 / area0)*100
porcentagem_perda = 100-porcentagem_aprov
print("Porcentagem de aproveitamento Retrato: %.2f" %porcentagem_aprov, "%")
print("Porcentagem de perda Retrato: %.2f" %porcentagem_perda, "%")
