def função(T):
    T2 = []
    for i in range(len(T)):
        if (len(str(T[i])) >= 4):
            T2.append(T[i])
    print(T2)
    

função([1561,9,7854,0,123,74,2530])
