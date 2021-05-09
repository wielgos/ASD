# Mikolaj Wielgos

from copy import deepcopy


def euler(G):
    def dfsvisit(u):
        nonlocal non_euler

        visited[u] = True

        if non_euler:
            return  # zakanczamy wszystkie rekurencje, bo wiemy ze graf nie moze byc eulerowski
        if index[u] == 0:  # w takim wypadku nie będziemy w stanie pójść gdziekolwiek
            return

        while index[u] > 0:  # dopoki będziemy mogli przechodzic po krawedziach dla danego wierzcholka
            index[u] -= 1  # przechodzimy na kolejną krawędź (czy mozemy sprawdzamy potem w ifie)
            v = index[u]  # v to potencjalny wierzcholek na ktory się udamy
            if GG[v][u] == 1:  # sprawdzamy czy dana krawedz istnieje
                print(u, v)
                GG[v][u] = 0  # usuwamy dana krawedz
                GG[u][v] = 0  # usuwamy dana krawedz
                deg[u] += 1  # zliczamy stopien u i v
                deg[v] += 1  # zliczamy stopien u i v
                dfsvisit(v)

        if deg[u] % 2 == 1:  # jezeli po przetworzeniu wierzcholka ma on stopien nieparzysty
            non_euler = True
        cycle.insert(0, u)  # dodaję na początek listy z cyklem przetworzony wierzcholek 'u'

    n = len(G)
    GG = [[0] * n for _ in range(n)]
    deg = [0] * n  # lista z stopniami wierzcholkow
    for i in range(n):  # skopiowanie by nie niszczyć G
        for j in range(n):
            GG[i][j] = G[i][j]

    non_euler = False
    visited = [False] * n
    cycle = []  # inicjalizuję pustą listę by do niej insertować przetworzone wierzcholki
    index = [n] * n  # inicjalizuję listę z potencjalnymi mozliwymi przejsciami do wierzcholkow
    # potencjalne przejscia znajdują się od [0,n), dlatego wyzej najpierw odejmuję 1

    dfsvisit(0)  # wywolujemy dfsvisit

    for i in range(n):
        if visited[i] == False:  # sprawdzenie spojnosci grafu
            print("nie jest spojny")
            return None
    if non_euler:
        return None  # none bo był nieeulerowski
    else:
        return cycle  # zwracamy dany cykl


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


# G = [[0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 1],
#      [1, 1, 0, 0, 1, 1],
#      [0, 1, 0, 0, 0, 1],
#      [0, 0, 1, 0, 0, 1],
#      [0, 1, 1, 1, 1, 0]]

G = [[0, 1, 1, 1, 0, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 1, 0],
     [1, 1, 1, 0, 1, 0],
     [0, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 0, 0]]

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
