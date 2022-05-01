def intersec(A,B):
    C=[]
    for i in A:
        if i in B:
            C.append(i)
    return (C)

A = [7, 2, 5, 8, 4]
B= [4, 2,  5]
print(intersec(A,B))
