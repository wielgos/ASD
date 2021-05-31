from collections import deque


# floyd warshall
# graf nie moze zawierać ujemnych cykli
# najkrotsza sciezka miedzy dowolna para wierzcholkow
# krawedzie zarowno dodatnie jak i ujemne
# O(V^3)


def floydwarshall(G):  # G to macierz sąsiedztwa
    n = len(G)
    S = [[float('inf')] * (n) for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] is not None:
                S[u][v] = G[u][v]
                parent[u][v] = u

    for t in range(1, n):  # (t,n) ? (t, n+1)?
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]
                    parent[u][w] = parent[t][w]

    return S, parent


def path(parent, u, v):
    path = [v]
    while u != v:
        v = parent[u][v]
        path.insert(0, v)
    return path


if __name__ == '__main__':
    G = [[None, -2, 4],
         [-2, None, 1],
         [4, 1, None]]
    # ^ ujemny cykl
    G3 = [[None, 2, 4, None],
          [2, None, 1, -3],
          [4, 1, None, None],
          [None, None, None, None]]
    s, p = floydwarshall(G3)
    for e in p:
        print(e)
    print()
    print(s[0][3])
    print(path(p,0,3))
