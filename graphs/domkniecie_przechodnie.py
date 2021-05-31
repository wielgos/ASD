# floyd warshall
# graf nie moze zawierać ujemnych cykli
# najkrotsza sciezka miedzy dowolna para wierzcholkow
# krawedzie zarowno dodatnie jak i ujemne
# O(V^3)


def domkniecie(G):  # G to macierz sąsiedztwa
    n = len(G)
    for t in range(n):
        for u in range(n):
            for w in range(n):
                G[u][w] = G[u][w] or (G[u][t] and G[t][w])
    return G

if __name__ == '__main__':
    G = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    H = domkniecie(G)
    for e in H:
        print(e)
