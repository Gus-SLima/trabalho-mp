def Velha(matriz):
    c=0
    x=0
    v=0
    for i in range(3):
        for k in range(3):
            if matriz[i][k]==2:
                c+=1
            elif matriz[i][k]==1:
                x+=1
            else:
                v+=1
    if x-c>1 or x-c<0:
        return -2