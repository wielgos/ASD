# Mikołaj Wielgos
# Do  znalezienia  "najtańszego"  cyklu  wykorzystuję  algorytm  Dijkstry.
# Dla  każdej  krawędzi  w  grafie, usuwam  ją, i  sprawdzam  jaka  teraz  dzieli  odległość  wierzchołków,
# których  ta  krawędź  łączyła. Jeżeli  taka  odległość  istnieje(nie  rozspójniłem  grafu) to  po
# dołączeniu  tej  krawędzi  mam  cykl, którego  koszt  całkowity  to  odległość
# wcześniej  policzona + waga  usuniętej  krawędzi.
# W wypadku gdybym rospójnił graf, to dana odległość to float('inf'), jeżeli nie znajdę żadnej lepszej możliwości,
# to wiem, że nie ma żadnego cyklu.
# Złożoność czasowa to O(E^2logV), ze względu że dla każdej krawędzi wywołujemy Dijkstrę
# Jest to złożoność z małą stałą, ze wzgłedu na to, że zaimplementowałem możliwość zmiany klucza w kopcu
# (w kolejce priorytetowej jest co najwyżej V elementów)

from copy import deepcopy
from collections import deque


class MinHeap:  # [key, value]
    def __init__(self, length=0):
        self.elements = []
        self.size = 0
        self.H = [-1] * length
        self.idx = 0

    def b_down(self, i):  # O(logn)
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < self.size and self.elements[l][0] < self.elements[m][0]:
            m = l
        if r < self.size and self.elements[r][0] < self.elements[m][0]:
            m = r
        if m != i:
            self.elements[i][0], self.elements[m][0] = self.elements[m][0], self.elements[i][0]
            self.H[i], self.H[m] = self.H[m], self.H[i]
            self.b_down(m)

    def b_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.elements[i][0] < self.elements[parent][0]:
            self.elements[i][0], self.elements[parent][0] = self.elements[parent][0], self.elements[i][0]
            self.H[i], self.H[parent] = self.H[parent], self.H[i]
            self.b_up(parent)

    def put(self, v):  # append + O(log n)
        self.elements.append(v)
        self.size += 1
        self.H[self.idx] = self.size - 1
        self.idx += 1
        self.b_up(self.size - 1)

    def pop(self):
        result = self.elements[0][1]
        self.elements[0] = self.elements[self.size - 1]
        self.b_down(0)
        self.size -= 1
        return result

    def change_key(self, idx, key):  # operacja zmiany klucza, po zmianie muszę odpowiednio poprawić kopiec
        if key < self.elements[self.H[idx]][0]:
            self.elements[self.H[idx]][0] = key
            self.b_up(self.H[idx])
        else:
            self.elements[self.H[idx]][0] = key
            self.b_down(self.H[idx])


def min_cycle(G):
    def dijkstra(G, s):  # G to macierz sąsiedztwa
        n = len(G)
        d = [float('inf')] * n
        parent = [None] * n
        d[s] = 0
        minh = MinHeap(n)  # inicjalizuję mój customowy kopiec min z możliwością zmiany klucza
        for i in range(n):
            minh.put([float('inf'), i])  # dodaję wszystkie wierzchołki do kopca z priorytetem 'inf'

        while minh.size != 0:  # dopoki kopiec nie jest pusty
            u = minh.pop()  # pobieram wierzcholek
            for v in range(n):
                if G[u][v] >= 0 or G[u][v] >= 0:  # jeżeli dana krawędź istnieje (istnieje -> wartość nieujemna)
                    if d[v] > d[u] + G[u][v]:  # relaksacja
                        d[v] = d[u] + G[u][v]
                        parent[v] = u
                    minh.change_key(v, d[v])  # O(logn), zmiana wartości klucza, od nowa pozycjonuje dany element
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
