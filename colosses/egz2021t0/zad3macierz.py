from colosses.asdt0.zad3testy import runtests
from queue import PriorityQueue


def dijkstra2(G, s, dest):  # G to macierz sąsiedztwa
    n = len(G)
    done = [[False] * n for _ in range(2)]
    d = [[float('inf')] * n for _ in range(2)]
    d[0][s] = 0
    d[1][s] = 0
    while not done[0][dest] and not done[1][dest]:
        # get 0
        u = -1
        d_best = float('inf')
        for j in range(n):
            if not done[0][j] and d[0][j] <= d_best:
                u = j
                d_best = d[0][j]
        # got best for 0
        for v in range(n):
            if G[u][v] > 0:
                if d[0][v] > d[0][u] + G[u][v]:
                    d[0][v] = d[0][u] + G[u][v]
                for v2 in range(n):
                    if G[v][v2] > 0:
                        w = max(G[u][v], G[v][v2])
                        if d[1][v2] > d[0][u] + w:
                            d[1][v2] = d[0][u] + w
        done[0][u] = True
        u = -1
        d_best = float('inf')
        for j in range(n):
            if not done[1][j] and d[1][j] <= d_best:
                u = j
                d_best = d[1][j]

        for v in range(n):
            if G[u][v] > 0:
                if d[0][v] > d[1][u] + G[u][v]:
                    d[0][v] = d[1][u] + G[u][v]
        done[1][u] = True
    return min(d[0][dest], d[1][dest])


def jumper(G, s, w):
    return dijkstra2(G, s, w)


runtests(jumper)
