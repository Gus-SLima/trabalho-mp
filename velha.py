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
    for i in range(3):
        if matriz[i][0]==matriz[i][1] and matriz[i][1]==matriz[i][2]:
            if matriz[i][0]==1:
                return 1
            else:
                return 2
        elif matriz[0][i]==matriz[1][i] and matriz[1][i]==matriz[2][1]:
            if matriz[i][0]==1:
                return 1
            else:
                return 2