from queue import PriorityQueue
from collections import deque


# E LOG V
# more precise: Elog(E), but log(E) is the same as log(V) in big O
# slower by constant because of lacking decrease-key operation

def dijkstra(G, s):  # G to macierz sąsiedztwa
    def relax(u, v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u
            return 1
        return 0

    n = len(G)
    Q = PriorityQueue()
    d = [float('inf')] * n
    parent = [None] * n
    done = [False] * n
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        trash, u = Q.get()
        if done[u]:
            continue
        for v in range(n):
            if G[u][v] > 0 and relax(u, v):
                Q.put((d[v], v))
        done[u] = True
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
    d, p = dijkstra(G, 0)
    print(d)
    print(p)
    print(path(p, 1))
