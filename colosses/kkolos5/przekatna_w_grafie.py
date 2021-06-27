from colosses.kkolos5.przekatna_w_grafietesty import runtests


def przekatna_w_grafie(G) -> int:
    def floydwarshall(G):  # G to macierz sąsiedztwa
        n = len(G)
        S = [[float('inf')] * (n) for _ in range(n)]

        for u in range(n):
            for v in range(n):
                if G[u][v] > 0:
                    S[u][v] = G[u][v]

        for t in range(1, n):
            for u in range(n):
                for w in range(n):
                    if S[u][w] > S[u][t] + S[t][w]:
                        S[u][w] = S[u][t] + S[t][w]

        return S
    n = len(G)
    # for i in range(n):
    #     cnt = 0
    #     for j in range(n):
    #         if G[i][j] <= 0:
    #             cnt += 1
    #     if cnt == n:
    #         print("niespojny??")
    #         return None #nie jest spojny
    S = floydwarshall(G)

    maks = -1
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if S[i][j] != float('inf'):
                maks = max(S[i][j], maks)
    # if maks > 0:
    #     print(maks)
    # else:
    #     print("None")
    return maks if maks > 0 else None


runtests(przekatna_w_grafie)
