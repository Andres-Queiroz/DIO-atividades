a = int(input())
b = int(input())
count = 0
#while (a > b) or (a <= 0 or b >= 9999):
#    a = int(input('digite novamente '))
#    b = int(input('digite novamente '))
        
for a in range (a, b+1):
   if (a %400 == 0) or (a %4 ==0 and a %100 != 0):
        print(a)
        count += 1       
print(f'bissextos: {count}')
