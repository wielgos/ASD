# Algorytm Edmonda-Karpa

# O(VE^2)

def max_flow(G, s, t):
    n = len(G)  # Capacity matrix
    F = [[0] * n for i in range(n)]
    path = BFS(G, F, s, t)  # szukam dowolnej ścieżki do ujścia
    #  print path
    while path != None:
        flow = min(G[u][v] - F[u][v] for u, v in path)  # uzupełniam flow
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = BFS(G, F, s, t)  # szukam scieżki powiększającej
    return sum(F[s][i] for i in range(n))  # zwracam sume flow'ów do danego ujścia


def BFS(G, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(G)):
            if (G[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


G = [[0, 3, 0, 3, 0, 0, 0],
     [0, 0, 4, 0, 0, 0, 0],
     [3, 0, 0, 1, 2, 0, 0],
     [0, 0, 0, 0, 2, 6, 0],
     [0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 0, 0, 0]]
maks = max_flow(G, 0, 5)
print(maks)
# max flow is 4
