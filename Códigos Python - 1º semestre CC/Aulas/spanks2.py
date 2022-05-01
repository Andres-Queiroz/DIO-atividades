valor = float(input())

print("NOTAS: ")
valor1 = valor//100
numero1 = valor - (valor1*100)
valor2 = numero1 // 50
numero2 = numero1 - (valor2*50)
valor3 = numero2 // 20
numero3 = numero2 - (valor3*20)
valor4 = numero3 // 10
numero4 = numero3 - (valor4*10)
valor5 = numero4 // 5
numero5 = numero4 - (valor5*5)
valor6 = numero5 // 2
numero6 = numero5 - (valor6*2)

print("%.i" %valor1, "nota(s) de R$ 100.00")
print("%.i" %valor2,"nota(s) de R$ 50.00")
print("%.i" %valor3,"nota(s) de R$ 20.00")
print("%.i" %valor4,"nota(s) de R$ 10.00")
print("%.i" %valor5,"nota(s) de R$ 5.00")
print("%.i" %valor6,"nota(s) de R$ 2.00")

print("MOEDAS: ")
moeda1 = numero6 // 1
m1 = numero6 - (moeda1*1)
moeda2 = m1 // 0.5
m2 = m1 - (moeda2*0.5)
moeda3 = m2 // 0.25
m3 = m2 - (moeda3*0.25)
moeda4 = m3 // 0.10
m4 = m3 - (moeda4*0.10) 
moeda5 = m4 // 0.05
m5 = m4 - (moeda5*0.05) 
moeda6 = m5 // 0.01
m6 = m5 - (moeda6*0.01)
print("%.i" %moeda1, "moeda(s) de R$ 1.00")
print("%.i" %moeda2, "moeda(s) de R$ 0.50")
print("%.i" %moeda3, "moeda(s) de R$ 0.25")
print("%.i" %moeda4, "moeda(s) de R$ 0.10")
print("%.i" %moeda5, "moeda(s) de R$ 0.05")
print("%.i" %moeda6, "moeda(s) de R$ 0.01")
