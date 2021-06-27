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

from colosses.kolos3.zad1testy import runtests
from collections import deque


# mam wrażenie, że warunek sprawdzający jest źle
def check(x1, y1, x2, y2, d, M, S):  # warunek sprawdzający i łączący dane wierzchołki-krotki
    if M[x1][x2] != 0 and M[y1][y2] != 0 and x1 == y2 and x2 == y1:
        return False
    if S[x1][y1] >= d and S[x2][y2] >= d and M[x1][x2] != 0 and M[y1][y2] != 0:
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
        S[u][u] = 0

    for t in range(1, n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S


def path(parent, s, krotki):  # funkcja zwracająca ścieżke
    path = []
    while s != -1:
        path.append(krotki[s])
        s = parent[s]
    return path[::-1]


def keep_distance(M, x, y, d):
    S = floydwarshall(M)
    n = len(M)
    k = n ** 2
    G = [[0] * k for _ in range(k)]
    krotki = []
    start = -1
    end = -1
    for i in range(n):
        for j in range(n):
            if i == x and j == y:
                start = len(krotki)
            if i == y and j == x:
                end = len(krotki)
            krotki.append((i, j))
        M[i][i] = 1
    # print(krotki)
    for i in range(len(krotki)):
        for j in range(len(krotki)):
            if i == j:
                continue
            x1 = krotki[i][0]
            y1 = krotki[i][1]
            x2 = krotki[j][0]
            y2 = krotki[j][1]
            if check(x1, y1, x2, y2, d, M, S):
                G[i][j] = 1
                # print(krotki[i],krotki[j])
    parent = BFS(G, start)
    # print(start, krotki[start])
    # print(end, krotki[end])
    # print(parent)
    return path(parent, end, krotki)


runtests(keep_distance)
