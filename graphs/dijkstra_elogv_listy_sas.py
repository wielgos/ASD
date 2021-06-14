from queue import PriorityQueue
from collections import deque


# (V+E) LOG V high constant unfortunately

def dijkstra(G, s):  # G to macierz sąsiedztwa
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    n = len(G)
    d = [float('inf')] * n
    parent = [None] * n
    done = [False] * n
    d[s] = 0
    Q = PriorityQueue()

    for i in range(n):
        Q.put((d[i], i))

    while not Q.empty():
        trash, u = Q.get()
        if done[u]:
            continue
        for v, w in G[u]:
            relax(u, v, w)
            Q.put((d[v], v))
        done[u] = True
    return d, parent


def path(parent, s):
    path = []
    while s is not None:
        path.append(s)
        s = parent[s]
    return path[::-1]


if __name__ == '__main__':
    G = [[(1, 2), (2, 4)],
         [(0, 2), (2, 1)],
         [(0, 4), (1, 1)]]
    d, p = dijkstra(G, 0)
    print(d)
    print(p)
    print(path(p, 1))
