def TS(G):
    def DFSvisit(G, u):
        nonlocal time
        nonlocal i

        time += 1
        visited[u] = True

        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                DFSvisit(G, v)

        time += 1
        res[i] = u
        i -= 1

    n = len(G)
    i = n - 1
    res = [None]*n
    visited = [False] * n
    time = 0

    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(G, u)

    return res

def createAdjMatrix(L):  # stworz macierz sąsiedztwa bazując na liscie krawedzi
    n = -1
    for i in range(len(L)):
        n = max(L[i][0], L[i][1], n)
    n += 1

    M = [[0] * n for _ in range(n)]
    for i in range(len(L)):
        M[L[i][0]][L[i][1]] = 1
    return M


if __name__ == "__main__":
    G = [[0, 1, 0, 0, 1, 1],
         [0, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]
    v = TS(G)
    print(v)
