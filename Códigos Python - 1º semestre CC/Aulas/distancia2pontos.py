x1_y1 = input()
x1, y1 = x1_y1.split()
x1 = float(x1)
y1 = float(y1)

x2_y2 = input()
x2, y2 = x2_y2.split()
x2 = float(x2)
y2 = float(y2)

d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print("{:.4f}".format(d))

X1_Y1 = input()
X1, Y1 = X1_Y1.split()
X1 = float(X1)
Y1 = float(Y1)

X2_Y2 = input()
X2, Y2 = X2_Y2.split()
X2 = float(X2)
Y2 = float(Y2)

VALOR = (((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** 0.5
print("{:.4f}".format(VALOR))
