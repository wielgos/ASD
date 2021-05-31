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
                    return d, parent, True

    return d, parent, False  # false - nie znaleziono ujemnego cyklu


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
    d, p, b = bellmanford(G3, 0)
    print(d[3])
    print(d)
    print(p)
    print(b)
    print(path(p, 3))
