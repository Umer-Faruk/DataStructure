def spiral(mat):
    n = len(mat)
    m= len(mat[0])
    T = L = 0
    B= n-1
    R = m-1
    dirt = 0
    sp = []
    while T<=B and L<=R:
        if dirt == 0:
            for i in range(L,R+1):
                sp.append(mat[T][i])
            T += 1
        elif dirt == 1:
            for i in range(T,B+1):
                sp.append(mat[i][R])
            R -= 1
        elif dirt == 2:
            for i in range(R,L-1,-1):
                sp.append(mat[B][i])
            B -= 1
        elif dirt == 3:
            for i in range(B,T-1,-1):
                sp.append(mat[i][L])
            L += 1
        dirt = (dirt+1)%4
    return sp
    
l = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]]
 
print(spiral(l))