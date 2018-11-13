
def apsp(W):
    #
    # Inner Function Definitions
    #
    def newMatrix(size):
        M = []
        for _ in range(size):
            m = [float('inf')] * size
            M.append(m)
        return M

    def ExtendShortestPaths(L, a, b):
        if L[a] is None:
            L[a] = ExtendShortestPaths(L, a//2, a - a//2)
        if L[b] is None:
            L[b] = ExtendShortestPaths(L, b//2, b - b//2)
        n = len(l[a])
        M = newMatrix(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    M[i][j] = min(M[i][j], L[a][i][k] + L[b][k][j])
        return M
    
    #
    # Main function definition
    #

    n = len(W) -1 # since longest possible path is number of vertices -1
    L = [None] * (n+1) # initialzie L, the matrix of Matrix powers
    L[1] = W
    
    # Create L[0]
    
    l = newMatrix(n)
    for i in range(n):
        l[i][i] = 1
    L[0] = l
    
    L[n] = ExtendShortestPaths(L, n//2, n - n//2)
    return L
    
