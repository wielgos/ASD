# Mikołaj Wielgos
# Algorytm wyszukujący ścieżke Eulera, bazowałem na wykładzie i 2 krokach ->
# 1. wykonaj zwykły DFS
# 2. na bieżąco usuwaj krawędzie po których chodzisz, i po przetworzeniu wierzchołka dodaj go na początek listy
# W algorytmie dodatkowo na bieżąco liczę sobie stopnie wierzchołków, przez co, gdy po przetworzeniu będzie on miał nieparzysty stopień,
# to wiem, że graf nie może mieć cyklu Eulera. Dodatkowo, jeżeli okaże się, że graf jest niespójny (jednym dfsvisit nie odwiedzę każdego wierzchołka),
# to również nie może być eulerowski.
# jeżeli algorytm nie napotka wyżej wymienionych problemów, to zgodnie z zbudowaną listą z kroku 2. zwracam ją jako trasę cyklu Eulera
# nie tworzę dodatkowej tablicy, tylko działam na G, dokładniej na elementach nad przekątną, na koniec przywracam ją do stanu początkowego
# korzystając z elementow pod przekątną (bo jest to graf nieskierowany, więc elementy są odbite względem przekątnej).
from copy import deepcopy
from collections import deque


def euler(G):
    def dfsvisit(u):
        nonlocal non_euler  # nonlocal, by znać stan zmiennej logicznej w każdym momencie rekurencji -> by potem szybko ją zakończyć

        visited[u] = True  # bo wlasnie odwiedzamy wierzcholek u

        if non_euler:
            return  # zakanczamy wszystkie rekurencje, bo wiemy ze graf nie moze byc eulerowski
        for v in range(n):  # sprawdzamy dostępne krawędzie
            if v < u:  # bo korzystam tylko z elementów nad przekątną macierzy więc muszę mieć v<u, inaczej wywołuję G[u][v]
                if G[v][u] == 1:
                    G[v][u] = 0
                    deg[u] += 1  # zliczamy stopien u i v
                    deg[v] += 1  # zliczamy stopien u i v
                    dfsvisit(v)  # odwiedzamy v
            else:
                if G[u][v] == 1:
                    G[u][v] = 0
                    deg[u] += 1  # zliczamy stopien u i v
                    deg[v] += 1  # zliczamy stopien u i v
                    dfsvisit(v)  # odwiedzamy v

        if deg[u] % 2 == 1:  # jezeli po przetworzeniu wierzcholka ma on stopien nieparzysty
            non_euler = True  # to wiem ze graf nie jest eulerowski
        cycle.append(u)  # dodaję do kolejki z cyklem przetworzony wierzcholek 'u' O(1)

    n = len(G)
    deg = [0] * n  # lista z stopniami wierzcholkow
    non_euler = False  # zmienna logiczna, dzieki niej będę mógł skończyć szybciej rekurencję
    visited = [False] * n  # na początku żadnego wierzchołka nie odwiedziłem
    cycle = deque()  # inicjalizuję pustą listę by do niej insertować przetworzone wierzcholki

    dfsvisit(0)  # wywolujemy dfsvisit
    for i in range(n):  # przywracam G do stanu początkowego
        for j in range(i + 1, n):
            if G[j][i] == 1:
                G[i][j] = 1

    for i in range(n):
        if visited[i] == False:  # sprawdzenie spojnosci grafu (jezeli jednym dfsvisit nie odwiedzilem wszystkich)
            return None  # to wiem ze nie jest spojny, czyli nie moze byc eulerowski
    if non_euler:
        return None  # none bo był nieeulerowski
    else:
        cycleL = [0] * len(cycle)  # mam zwrócić listę z kolejnymi wierzchołkami
        index = 0
        while cycle:
            cycleL[index] = cycle.pop()  # zdejmuję z kolejki elementy i dodaję je do listy
            index += 1
        return cycleL


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)
if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
