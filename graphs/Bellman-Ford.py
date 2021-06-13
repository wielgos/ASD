from collections import deque


# normally E*V, ale:
# Wersja macierzowa, V^3
# najkrotsza sciezka w grafie z wagą dowolną

def bellmanford(G, s):  # G to macierz sąsiedztwa
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    n = len(G)
    d = [float('inf')] * n
    parent = [None] * n
    d[s] = 0

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] is not None:
                    relax(u, v, G[u][v])
    for u in range(n):
        for v in range(n):
            if G[u][v] is not None:
                if d[v] > d[u] + G[u][v]:
                    return False  # not correct

    return d, parent, True  # correct


def bellmanford2(G, s):  # G to lista sasiedztwa
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    n = len(G)
    d = [float('inf')] * n
    parent = [None] * n
    d[s] = 0

    for i in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                relax(u, v, w)
    for u in range(n):
        for v, w in G[u]:
            if d[v] > d[u] + w:
                return False

    return d, parent  # false - nie znaleziono ujemnego cyklu


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
    G = [[None, -2, 4],
         [-2, None, 1],
         [4, 1, None]]
    # ^ ujemny cykl
    G3 = [[None, 2, 4, None],
          [2, None, 1, -3],
          [4, 1, None, None],
          [None, None, None, None]]
    G1 = [[(1, 4), (3, 5)], [(3, 5)], [(1, -10)], [(2, 3)]]
    s1 = 0
    print(bellmanford2(G1, s1))

    G2 = [[(1, 6), (2, 5), (3, 5)], [(4, -1)], [(1, -2), (4, 1)], [(2, -2), (5, -1)], [(6, 3)], [(6, 3)], []]
    s2 = 0
    print(bellmanford2(G2, s2))
