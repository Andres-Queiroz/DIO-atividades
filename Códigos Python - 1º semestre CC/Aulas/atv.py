a_b_c = input()
a,b,c = a_b_c.split()
a = int(a)
b = int(b)
c = int(c)

maior_ab = ((a+b+abs(a-b))/2)
maior_abc = ((maior_ab+c+abs(maior_ab-c))/2)

print('%.0f' %maior_abc, 'eh o maior')
