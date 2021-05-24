from collections import deque


#  V^2  -> TRUE VERSION

def dijkstra(G, s):  # G to macierz sąsiedztwa
    def relax(u, v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    d = [float('inf')] * n

    parent = [None] * n
    visited = [False] * n
    d[s] = 0

    for i in range(n):
        u = -1
        d_best = float('inf')
        for j in range(n):
            if not visited[j] and d[j] <= d_best:
                u = j
                d_best = d[j]
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                relax(u, v)
    return d, parent


def pathrec(parent, s):
    if s is not None:
        pathrec(parent, parent[s])
        print(s, end=" ")


def path(parent, s):
    path = deque()
    len = 0
    while s is not None:
        path.append(s)
        s = parent[s]
        len += 1
    pathL = [0] * len
    for i in range(len):
        pathL[i] = path.pop()
    return pathL


if __name__ == '__main__':
    G = [[0, 10, 0, 0, 0, 0, 1],
         [10, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0]]

    G2 = [[0, 2, 4],
          [2, 0, 1],
          [4, 1, 0]]

    G3 = [[0, 2, 4, 0],
          [2, 0, 1, 0],
          [4, 1, 0, 0],
          [0, 0, 0, 0]]
    G4 = [[0, 6, 0, 0],
          [6, 0, 6, 0],
          [0, 6, 0, 6],
          [0, 0, 6, 0]]
    d, p = dijkstra(G4, 0)
    print(d)
    print(p)
    print(path(p, 1))
