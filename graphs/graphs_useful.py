def createAdjMatrix(L):  # stworz macierz sąsiedztwa bazując na liscie krawedzi
    n = -1
    for i in range(len(L)):
        n = max(L[i][0], L[i][1], n)
    n += 1

    M = [[0] * n for _ in range(n)]
    for i in range(len(L)):
        M[L[i][0]][L[i][1]] = 1
    return M

def createNeighList(G):
    n = len(G)
    L = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                L[i].append(j)
    return L

def is_connected(G):
    def DFSvisit(G, u):
        visited[u] = True

        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                DFSvisit(G, v)
    n = len(G)
    visited = [False] * n
    DFSvisit(G, 0)
    for i in range(n):
        if not visited[i]:
            return False
    return True
