from collections import deque


def dwudzielny(G):
    def dwudzielny_bfs(G, s):  # G is a list of GraphNodes, s is starting vertex
        Q = deque()
        if d[s] == -1:
            d[s] = 0
        Q.append(s)  # we put index of vertex, to get data we use G[s]
        while Q:
            u = Q.pop()
            if d[u] == 0:
                num = 1
            else:
                num = 0
            for v in range(n):
                if G[u][v] == 1:  # istnieje krawedz u->v
                    if d[v] == -1:
                        d[v] = num
                        Q.append(v)
                    elif d[v] != num:
                        return False
        return True

    n = len(G)
    d = [-1] * n

    for i in range(n):
        if not dwudzielny_bfs(G, i):
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


if __name__ == '__main__':
    L = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 4), (2, 5), (3, 0), (3, 5), (3, 4), (4, 1), (4, 2), (4, 3),
         (5, 2), (5, 3)]
    # G = createadjmatrix(L)
    # G = [[0,1,0,0],
    #      [1,0,1,1],
    #      [0,1,0,1],
    #      [0,1,1,0]]
    # 0 --- 1 --- 2 --- 3
    #        \_________/
    # nie jest dwudzielny
    G = [[0, 1, 0, 0],
         [1, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]]
    # 0 --- 1       2 --- 3
    # jest dwudzielny
    print(dwudzielny(G))
