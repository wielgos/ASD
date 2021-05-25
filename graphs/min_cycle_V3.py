# Mikołaj Wielgos
# Do  znalezienia  "najtańszego"  cyklu  wykorzystuję  algorytm  Dijkstry.
# Dla każdego wierzchołka grafu G(V,E), uruchamiam algorytm Dijkstry. Jeżeli podczas obliczania najkrótszych odległości
# Napotkam wierzchołek j , który już ma odległość policzoną, to wiem, że mogę dokonać trasy źródło - j - i - źródło
# I to będzie mój cykl o wartości d[i] + d[j] + G[i][j]. Wartość takiego cyklu zliczam i obliczam trasę, jeżeli znajdę
# lepszy, to podmieniam itd.
# Złożoność Dijkstry to V^2 - wersja zoptymalizowana dla macierzy z "kolejką" jako tablicą odległości.
# Więc całkowita złożoność algorytmu to O(V^3) [ dla każdego wierzchołka Dijkstra ]

from copy import deepcopy
from collections import deque


def min_cycle(G):
    def path(parent, v1, v2):  # do uzyskiwania trasy typu źródło -> v1 -> v2 -> źródło
        path = deque()
        len = 0
        while v1 is not None:
            path.appendleft(v1)
            v1 = parent[v1]
            len += 1
        while v2 is not None:
            path.append(v2)
            v2 = parent[v2]
            len += 1
            if parent[v2] is None:  # by nie powtarzać wierzchołka ze źródła 2 razy
                break
        pathL = [0] * len
        for i in range(len):
            pathL[i] = path.pop()
        return pathL

    def dijkstra(G, s):  # G to macierz sąsiedztwa
        nonlocal min_val, end_path

        # inicjalizacja początkowych zmiennych dla Dijkstry
        n = len(G)
        d = [float('inf')] * n
        parent = [None] * n
        visited = [False] * n
        d[s] = 0

        for i in range(n):
            u = -1
            d_best = float('inf')
            for j in range(n):
                if not visited[j] and d[j] <= d_best:  # "kolejka priorytetowa", wybieram najbliższy wierzchołek
                    u = j
                    d_best = d[j]
            visited[u] = True

            for v in range(n):  # sprawdzam jego sąsiadów
                if G[u][v] != -1 and not visited[v]:  # jeżeli ma sąsiada który nie został przetworzony
                    if d[v] != float('inf'):  # jeżeli napotkałem wierzchołek z obliczoną już odległością do źródła
                        cycle_value = d[u] + d[v] + G[u][v]  # to mogę utworzyć cykl
                        if cycle_value < min_val:  # jeżeli wartość cyklu jest najmniejsza do tej pory
                            min_val = cycle_value
                            end_path = path(parent, u, v)  # zapisuję trasę końcową
                    if d[v] > d[u] + G[u][v]:  # standardowa relakasacja krawędzi w Dijkstrze
                        d[v] = d[u] + G[u][v]
                        parent[v] = u

    # inicjalizacja początkowych zmiennych
    n = len(G)
    min_val = float('inf')
    end_path = []

    for i in range(n):  # dla każdego wierzchołka uruchamiam Dijkstrę
        dijkstra(G, i)  # wykonuje dijkstrę ze startem z wierzchołka i
        # dodatkowa uwaga: Dijkstra nie zwraca niczego, ponieważ podmienia mi zmienne globalne
    return end_path  # końcowa ścieżka, bądź jej brak znajduje się w end_path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

LEN = 7

GG = deepcopy(G2)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
