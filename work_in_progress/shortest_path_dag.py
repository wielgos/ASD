from collections import deque


def shortest_dag(G, s):
    def DFSvisit(G, u):
        print("enter", u)
        for v in range(len(G)):
            if G[u][v] == 0:
                continue

            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u

            deg[v] -= 1
            if deg[v] == 0:
                DFSvisit(G, v)

    n = len(G)
    parent = [None] * n
    deg = [0] * n

    d = [float('inf')] * n
    d[s] = 0

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                deg[u] += 1

    for v in range(len(G)):
        if G[s][v] != 0:
            DFSvisit(G, s)

    return parent, d


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


if __name__ == "__main__":
    G1 = [[0, 7, 0, 1, 0],
         [0, 0, 7, 0, 0],
         [0, 0, 0, 7, 0],
         [0, 0, 0, 0, 7],
         [0, 0, 0, 0, 0]]

    p, d = shortest_dag(G1, 0)

    print(p)
    print(d)
    print(path(p, 4))
