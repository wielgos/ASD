from colosses.asdt0.zad3testy import runtests
from queue import PriorityQueue


def dijkstra2(G, s, dest):  # G to macierz sąsiedztwa
    n = len(G)
    Q = PriorityQueue()
    done = [[False] * n for _ in range(2)]
    d = [[float('inf')] * n for _ in range(2)]
    d[0][s] = 0
    Q.put((0, s, 0))
    while not Q.empty():
        cur, u, but = Q.get()
        if done[but][u]:
            continue
        for v in range(n):
            if G[u][v] > 0:
                # print(f"cur:{cur},u:{u},but:{but}")
                # print(f"v:{v}")
                if but == 0:
                    if d[0][v] > d[0][u] + G[u][v]:
                        d[0][v] = d[0][u] + G[u][v]
                        Q.put((d[0][v], v, 0))
                    for v2 in range(n):
                        if G[v][v2] > 0:
                            w = max(G[u][v], G[v][v2])
                            if d[1][v2] > d[0][u] + w:
                                d[1][v2] = d[0][u] + w
                                Q.put((d[1][v2], v2, 1))
                elif but == 1:
                    if d[0][v] > d[1][u] + G[u][v]:
                        d[0][v] = d[1][u] + G[u][v]
                        Q.put((d[0][v], v, 0))
        done[but][u] = True
    return min(d[0][dest], d[1][dest])


def jumper(G, s, w):
    return dijkstra2(G, s, w)


runtests(jumper)
