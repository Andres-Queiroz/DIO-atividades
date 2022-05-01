s = str(input("S ")).lower()
p = str(input("P ")).lower()
k = str(input("K ")).lower()
sg = str(input("S(g)")).lower()

if (s == "couche1"):
    s = (1.0)

if (s == "couche2"):
    s = (1.2)

if (s == "semi"):
    s = (1.4)

if (s == "duplex"):
    s = (2)

if (s == "coated"):
    s = (1.5)

if (s == "offset"):
    s = (1.6)

if (s == "jornal"):
    s = (1.8)

if (s == "kraft"):
    s = (2.2)

#2

if (p == "tipografia"):
    p = (1.0)

if (p == "offset"):
    p = (0.5)
#3
a = float(input("Digite a área da impressão em metros "))
print(a)
#4
n = float(input("Digite a tiragem da impressão "))
print(n)
#5

if (k == "chapado"):
    k = (1.0)
if (k == "reticula de 70%"):
    k =(0.7)
if (k == "reticula de 40%"):
    k = (0.4)
if (k == "reticula de 30%"):
    k = (0.3)
if (k == "so texto"):
    k = (0.2)

#6

if sg == ("preto e prata"):
    sg =(1.0)
if sg == ("cores transparentes"):
    sg = (1.2)
if sg == ("cores opacas"):
    sg = (1.7)
if sg == ("branco opaco ou ouro"):
    sg = (2.0)

tinta = (s*p*a*n*k*sg)/353
'print(s, p, a, n, k, sg)'
print(f'A quantidade de tinta a ser usada será: {tinta:.2f} Kg(s) de tinta')

