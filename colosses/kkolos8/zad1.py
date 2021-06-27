def mlodszy_pasjonat(M, A, B, x, T):
    def bellmanford(G, s):  # G to macierz sąsiedztwa
        def relax(u, v, w):
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parent[v] = u
                return 1

        n = len(G)
        d = [float('inf')] * n
        parent = [None] * n
        d[s] = 0
        red = [0] * n
        for i in range(n):
            red[i] = x
        for i in range(n - 1):
            for u in range(n):
                for v in range(n):
                    if G[u][v] > 0 and (red[u] > 0 or T[v] != "czerwony"):
                        if T[v] == "czerwony":
                            if relax(u, v, G[u][v]):
                                red[v] = red[u] - 1
                        else:
                            if relax(u, v, G[u][v]):
                                red[v] = x

        for u in range(n):
            for v in range(n):
                if G[u][v] > 0 and (red[v] > 0 or T[v] != "czerwony"):
                    if T[v] == "czerwony":
                        if relax(u, v, G[u][v]):
                            return False
                    else:
                        if relax(u, v, G[u][v]):
                            return False

        return d, parent, True  # correct

    def path(parent, s, T):  # funkcja zwracająca ścieżke
        path = []
        while s is not None:
            path.append(s)
            s = parent[s]
        return path[::-1]

    d, par, R = bellmanford(M, A)
    print(path(par, B, T))
    return d[B]


from copy import deepcopy

M = [[0, 10, 0, 120, 0, 0, 1],
     [10, 0, 6, 0, 0, 0, 0],
     [0, 6, 0, 7, 0, 0, 0],
     [120, 0, 7, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 1, 0]]

T = ["biały", "biały", "czerwony", "czarny", "czerwony", "czerwony", "biały"]

A = 0
B = 3
x = 0
odp = [0, 3]
print(mlodszy_pasjonat(deepcopy(M), A, B, x, deepcopy(T)), odp)

x = 1
odp = [0, 1, 2, 3]
print(mlodszy_pasjonat(deepcopy(M), A, B, x, deepcopy(T)), odp)

x = 3
odp = [0, 6, 5, 4, 3]
print(mlodszy_pasjonat(deepcopy(M), A, B, x, deepcopy(T)), odp)
