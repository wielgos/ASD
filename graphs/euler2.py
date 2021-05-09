# Mikołaj Wielgos
# Algorytm wyszukujący ścieżke Eulera, bazowałem na wykładzie i 2 krokach ->
# 1. wykonaj zwykły DFS
# 2. na bieżąco usuwaj krawędzie po których chodzisz, i po przetworzeniu wierzchołka dodaj go na początek listy
# W algorytmie dodatkowo na bieżąco liczę sobie stopnie wierzchołków, przez co, gdy po przetworzeniu będzie on miał nieparzysty stopień,
# to wiem, że nie może mieć cyklu Eulera. Dodatkowo, jeżeli okaże się, że graf jest niespójny (jednym dfsvisit nie odwiedzę każdego wierzchołka),
# to również nie może być eulerowski.

from copy import deepcopy


def euler(G):
    def dfsvisit(u):
        nonlocal non_euler

        visited[u] = True  # bo wlasnie odwiedzamy wierzcholek u

        if non_euler:
            return  # zakanczamy wszystkie rekurencje, bo wiemy ze graf nie moze byc eulerowski
        for v in range(n):  # sprawdzamy dostępne krawędzie
            if GG[u][v] == 1 or GG[v][u] == 1:
                GG[v][u] = 0  # usuwamy dana krawedz
                GG[u][v] = 0  # usuwamy dana krawedz
                deg[u] += 1  # zliczamy stopien u i v
                deg[v] += 1  # zliczamy stopien u i v
                dfsvisit(v)  # odwiedzamy v

        if deg[u] % 2 == 1:  # jezeli po przetworzeniu wierzcholka ma on stopien nieparzysty
            non_euler = True  # to wiem ze graf nie jest eulerowski
        cycle.insert(0, u)  # dodaję na początek listy z cyklem przetworzony wierzcholek 'u'

    n = len(G)
    GG = [[0] * n for _ in range(n)]  # będzie służyła do przekopiowania G
    deg = [0] * n  # lista z stopniami wierzcholkow
    for i in range(n):  # skopiowanie by nie niszczyć G
        for j in range(n):
            GG[i][j] = G[i][j]

    non_euler = False  # zmienna logiczna twierdząca czy graf jest eulerowski
    visited = [False] * n  # na początku żadnego wierzchołka nie odwiedziłem
    cycle = []  # inicjalizuję pustą listę by do niej insertować przetworzone wierzcholki

    dfsvisit(0)  # wywolujemy dfsvisit

    for i in range(n):
        if visited[i] == False:  # sprawdzenie spojnosci grafu (jezeli jednym dfsvisit nie odwiedzilem wszystkich)
            print("nie jest spojny")  # to wiem ze nie jest spojny, czyli nie moze byc eulerowski
            return None
    if non_euler:
        return None  # none bo był nieeulerowski
    else:
        return cycle  # zwracamy dany cykl


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
print(cycle)
if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = 0
    GG[v][u] = 0
    u = v
print(GG)
for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
