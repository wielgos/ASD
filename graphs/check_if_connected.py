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


def createadjmatrix(L):  # stworz macierz sąsiedztwa bazując na liscie krawedzi
    n = -1
    for i in range(len(L)):
        n = max(L[i][0], L[i][1], n)
    n += 1

    M = [[0] * n for _ in range(n)]
    for i in range(len(L)):
        M[L[i][0]][L[i][1]] = 1
    return M


if __name__ == "__main__":
    L = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 4), (2, 5), (3, 0), (3, 5), (3, 4), (4, 1), (4, 2), (4, 3),
         (5, 2), (5, 3), (19, 20)]
    # L to lista krawędzi

    G = createadjmatrix(L)
    print(is_connected(G))
