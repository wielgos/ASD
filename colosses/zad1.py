# Mikołaj Wielgos

# Pomysł na algorytm:
# Wykonuję algorytm Floyda-Warshalla - przyda się od sprawdzania warunku z zadania
# następnie tworzę nowy graf z wierzchołkami typu (x1,y1) gdzie x1 to pozycja Carola a y1 to pozycja Marxa
# Teraz połączenie między (x1,y1) a (x2,y2) krawędzią następuje gdy jesteśmy w stanie przejść
# ze state (x1,y1) do (x2,y2)  -> uwaga może się zdarzyć że x1==x2 albo y1==y2 itp.
# Teraz po dokonaniu połączenia puszczam BFS ze źródła (x), by znaleźc najkrótszą trasę do y
# Zwracam najkrótszą trasę do y (w postaci krotek)
# Złożoność algorytmu O(V^3)
# *nie udało mi się zaimplementować do końca algorytmu, błąd przewiduję, że jest w funkcji check()

from colosses.zad1testy import runtests
from collections import deque


# mam wrażenie, że warunek sprawdzający jest źle
def check(x1, y1, x2, y2, d, M, S):  # warunek sprawdzający i łączący dane wierzchołki-krotki
    if M[x1][x2] == 0:
        return False
    if M[y1][y2] == 0:
        return False
    if S[x2][y2] >= d:
        return True
    return False


def BFS(G, s):  # BFS
    n = len(G)
    Q = deque()
    visited = [False] * n
    d = [-1] * n
    parent = [-1] * n
    d[s] = 0
    visited[s] = True
    Q.append(s)

    while Q:  # if deque is not empty
        u = Q.pop()
        for v in range(n):
            if G[u][v] == 1:
                if not visited[v]:
                    visited[v] = True
                    d[v] = d[u] + 1
                    parent[v] = u
                    Q.append(v)
    return parent


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


def path(parent, s):  # funkcja zwracająca ścieżke
    path = []
    while s is not None:
        path.append(s)
        s = parent[s]
    return path[::-1]


def keep_distance(M, x, y, d):
    S = floydwarshall(M)
    n = len(M)
    k = n ** 2
    G = [[0] * k for _ in range(k)]
    krotki = []
    for i in range(n):
        for j in range(n):
            krotki.append((i, j))
    print(krotki)
    for i in range(len(krotki)):
        for j in range(len(krotki)):
            x1 = krotki[i][0]
            y1 = krotki[i][1]
            x2 = krotki[j][0]
            y2 = krotki[j][1]
            if check(x1, y1, x2, y2, d, M, S):
                G[i][j] = 1
    parent = BFS(G, x)
    return path(parent, x)


runtests(keep_distance)
