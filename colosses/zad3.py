# Mikołaj Wielgos

# Mój algorytm polega na wyznaczeniu najkrótszych ścieżek między wierzchołkami używając Floyda-Warshalla,
# następnie tworzę nowy graf z 2 dodatkowymi wierzchołkami (super źródło, super ujście). Teraz odpowiednio łączę
# w graf dwudzielny ten graf -> wierzchołki 'green' mają krawędź skierowaną do 'blue'*, wygląda to tak:
#
#           G1 - - - B1
#         /        /    \
# super_S -  G2   /  B2  - super_T
#         \     /        /
#            G3 - - - B3
# (wszystkie krawędzie mają wagę 1)
# Następnie puszczam algorytm maxflow Edmondsa-Karpa, który znajduje mi maksymalne skojarzenie, w tym grafie dwudzielnym
# a co za tym idzie największą liczbę naturalną l spełniającą warunki zadania

# * Uwaga - zauważmy, że gdybym łączył B->G zamiast, G->B, to wynik byłby taki sam.

# Złożoność obliczeniowa:
#                        1. O(V^3) Floyd-Warshall, wyznaczenie odległości między każdym u,v
#                        2. O(V^2) Zbudowanie grafu na którym puścimy max-flow
#                        3. O(VE^2) Algorytm Edmonsa-Karpa (maxflow)
#                        --> Finalna złożoność to O(VE^2 + V^2 + V^3) = O(VE^2)
from colosses.zad3testy import runtests
from colosses.zad3EK import edmonds_karp


def floydwarshall(G):  # G to macierz sąsiedztwa, algorytm z wykładu
    n = len(G)
    S = [[float('inf')] * (n) for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                S[u][v] = G[u][v]

    for t in range(1, n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S


def BlueAndGreen(T, K, D):
    n = len(T)
    S = floydwarshall(T)  # zbieram odległosci miedzy kazdymi wierzcholkami
    # tworzę super graf z super zrodlem i super ujsciem
    G = [[0] * (n + 2) for _ in range(n + 2)]  # n+2, ponieważ dodam 2 wierzchołki
    # zakladam ze wierzcholek o indeksie n to zrodlo, a o indeksie n+1 to ujscie
    for i in range(n):
        for j in range(n):
            if S[i][j] >= D and K[i] == 'G' and K[j] == 'B':  # tworzę graf dwudzielny
                G[i][j] = 1  # łączę G z B krawędzia o wadze 1 gdy spełnia warunki zadania
    for i in range(n):  # uzupełniam krawędzie między super źródłem i super ujściem
        if K[i] == 'G':
            G[n][i] = 1  # krawedzie od zrodla do kazdego wierzcholka G
        if K[i] == 'B':
            G[i][n + 1] = 1  # krawedzie od kazdego B do super ujscia
    s = n  # indeks mojego super źródła
    t = n + 1  # indeks mojego super ujścia
    max_flow = edmonds_karp(G, s, t)
    return max_flow  # zwracam maxflow między s a t


runtests(BlueAndGreen)
