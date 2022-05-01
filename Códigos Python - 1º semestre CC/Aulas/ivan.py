students = int(input())
contador = 0
final_grade = 0
notas = 0
i = 0

first_list = []
new_list = []
final_list = []

while contador < students:
    first_grade = float(input())
    first_list.append(first_grade)
    contador += 1
contador = 0
while contador < students:
    new_grade = float(input())
    new_list.append(new_grade)
    if new_grade == 10.00:
        if first_list[i] >= 8.00:
            final_list.append(10.00)
        else:
            final_list.append(first_list[i] + 2.00)
    elif new_list[i] < 10.00:
        final_list.append(first_list[i])
    i += 1
    contador += 1

alteradas = 0
j = 0

while j < len(final_list):
    if first_list[j] != final_list[j]:
        alteradas += 1
    j += 1

j = 0
print('NOTAS ALTERADAS:', alteradas)
while j < len(final_list):
    if first_list[j] != final_list[j]:
        if final_list[j] == 10 and first_list[j] < 10:
            print("*(00{}) original: 0{:.2f} | final: {:.2f}".format(j+1, first_list[j], final_list[j]))
        elif final_list[j] < 10 and first_list[j] < 10:
            print("*(00{}) original: 0{:.2f} | final: 0{:.2f}".format(j+1, first_list[j], final_list[j]))
    elif first_list[j] == final_list[j]:
        if final_list[j] < 10 and first_list[j] < 10:
            print("-(00{}) original: 0{:.2f} | final: 0{:.2f}".format(j+1, first_list[j], final_list[j]))
        elif final_list[j] == 10 and first_list[j] == 10:
            print("-(00{}) original: {:.2f} | final: {:.2f}".format(j+1, first_list[j], final_list[j]))
        else:
            print("-(00{}) original: 0{:.2f} | final: 0{:.2f}".format(j+1, first_list[j], final_list[j]))
    j += 1
