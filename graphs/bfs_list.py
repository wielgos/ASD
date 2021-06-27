from collections import deque


def BFS(G, s):  # G to macierz sąsiedztwa
    n = len(G)

    Q = deque()
    visited = [False] * n
    d = [-1] * n
    parent = [-1] * n

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while Q:  # if deque is not empty
        u = Q.pop()
        for v in range(n):
            if G[u][v] == 1:
                if not visited[v]:
                    visited[v] = True
                    d[v] = d[u] + 1
                    parent[v] = u
                    Q.append(v)
    return visited, d, parent

def path(parent, s):  # funkcja zwracająca ścieżke
    path = []
    while s!=-1:
        path.append(s)
        s = parent[s]
    return path[::-1]

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
    # L to lista krawędzi

    M = createadjmatrix(L)
    # M to reprezentacja macierzowa na podstawie listy krawędzi

    LADJ = [[1, 2, 3], [0, 4], [0, 4, 5], [0, 5, 4], [1, 2, 3], [2, 3]]
    # LADJ to listy sąsiedztwa
    print()
    v, d, p = BFS(M, 0)
    print(path(p, 4))
    print(p)
