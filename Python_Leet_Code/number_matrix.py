def gen_matrix(n):

    List = [[0 for i in range(2*n-1)] for j in range(2*n-1)]
    for i in range(0, 2*n-1):
        for j in range(0,2*n-1):
            List[i][j] = max(i,j,((2*n-2)-i),((2*n-2)-j)) - n + 1

    print(List)

gen_matrix(4)   