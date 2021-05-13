from collections import deque


def gen_neigh(i, j, n):
    neigh = []
    if j + 1 < n:
        neigh.append(i * n + j + 1)  # to

    if j + (i + 1) * n < n * n and j < n:
        neigh.append(j + (i + 1) * n)

    if j + (i + 1) * n + 1 < n * n and j + 1 < n:
        neigh.append(j + (i + 1) * n + 1)
    return neigh


def c(i, j, n):
    return j + i * n


class GraphNode:
    def __init__(self):
        self.neigh = []
        self.visited = 0
        self.value = 0


def szachownica(G):
    n = len(G)
    GR = [GraphNode() for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            GR[c(i, j, n)].neigh = gen_neigh(i, j, n)
            GR[c(i, j, n)].value = 0
            print(i, j, GR[c(i, j, n)].neigh)

    GR[0].value = 0
    GR[0].visited = 1
    Q = deque()
    Q.append(0)
    while Q:  # if deque is not empty
        u = Q.pop()
        for v in GR[u].neigh:
            if not GR[v].visited:
                GR[v].value += GR[u].value + G[v // n][v % n]
                GR[v].visited = 1
            else:
                GR[v].value = min(GR[v].value, GR[u].value + G[v // n][v % n])
            Q.append(v)
    return GR[n * n - 1].value


G = [[0, 9, 9],
     [1, 1, 9],
     [1, 1, 1]]
print(szachownica(G))
