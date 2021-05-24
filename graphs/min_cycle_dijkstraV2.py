# Mikołaj Wielgos
# Do  znalezienia  "najtańszego"  cyklu  wykorzystuję  algorytm  Dijkstry.
# Dla  każdej  krawędzi  w  grafie, usuwam  ją, i  sprawdzam  jaka  teraz  dzieli  odległość  wierzchołków,
# których  ta  krawędź  łączyła. Jeżeli  taka  odległość  istnieje(nie  rozspójniłem  grafu) to  po
# dołączeniu  tej  krawędzi  mam  cykl, którego  koszt  całkowity  to  odległość
# wcześniej  policzona + waga  usuniętej  krawędzi.
# W wypadku gdybym rospójnił graf, to dana odległość to float('inf'), jeżeli nie znajdę żadnej lepszej możliwości,
# to wiem, że nie ma żadnego cyklu.
# Złożoność czasowa to O(V^4), ze względu że przechodzę przez macierz w V^2 i dla niektórych krawędzi rozpoczynam
# Dijkstrę w V^2

from copy import deepcopy
from collections import deque


def min_cycle(G):
    def dijkstra(G, s):  # G to macierz sąsiedztwa
        n = len(G)
        d = [float('inf')] * n
        parent = [None] * n
        visited = [False] * n
        d[s] = 0
        for i in range(n):
            u = -1
            d_best = float('inf')
            for j in range(n):
                if not visited[j] and d[j] <= d_best:
                    u = j
                    d_best = d[j]
            visited[u] = True
            for v in range(n):
                if G[u][v] > 0 and not visited[v]:
                    if d[v] > d[u] + G[u][v]:
                        d[v] = d[u] + G[u][v]
                        parent[v] = u
        return d, parent

    def path(parent, s):  # do uzyskiwania ścieżki, s - start
        path = deque()
        len = 0
        while s is not None:
            path.append(s)
            s = parent[s]
            len += 1
        pathL = [0] * len
        for i in range(len):
            pathL[i] = path.pop()
        return pathL

    # graf nieskierowany
    n = len(G)
    min_val = float('inf')  # inicjalizacja początkowych zmiennych
    best_start = -1
    best_parent = []

    for i in range(n):  # jest to graf nieskierowany więc działam na elementach nad przekątną
        for j in range(i + 1, n):
            if G[i][j] >= 0:  # jeżeli dana krawędź istnieje (istnieje -> wartość nieujemna)
                restore = G[i][j]  # by móc poźniej przywrócić daną krawędź
                G[i][j] = G[j][i] = -1  # usuwam tymczasowo krawędź między i,j
                d, parent = dijkstra(G, i)  # wykonuje dijkstrę ze startem z wierzchołka i
                if d[j] != float('inf'):  # jezeli nie rozspojnilismy grafu
                    value = d[j] + restore  # wartość cyklu to odległość od i do j (d[j]) + wczesniej usunieta krawedz
                    if value < min_val:  # podmieniam najlepsze znalezione wartości
                        min_val = value
                        best_parent = parent
                        best_start = j  # best start to j, ponieważ to od j do tyłu będziemy "skakać"
                G[i][j] = G[j][i] = restore  # przywracam krawędzie
    return path(best_parent, best_start) if min_val != float('inf') else []  # zwracam sciezke jezeli istnieje


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

LEN = 7

GG = deepcopy(G)
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
