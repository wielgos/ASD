# floyd warshall
# graf nie moze zawierać ujemnych cykli
# najkrotsza sciezka miedzy dowolna para wierzcholkow
# krawedzie zarowno dodatnie jak i ujemne
# O(V^3)


def domkniecie(G):  # G to macierz sąsiedztwa
    n = len(G)
    S = [[float('inf')] * (n) for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                S[u][v] = 1

    for t in range(n):  # (t,n) ? (t, n+1)?
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S


def path(parent, u, v):
    path = [v]
    while u != v:
        v = parent[u][v]
        path.insert(0, v)
    return path


if __name__ == '__main__':
    G = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    s = domkniecie(G)
    for e in s:
        print(e)
