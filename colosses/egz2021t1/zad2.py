# Mikołaj Wielgos
# Pomysł na algorytm:
# Najpierw tworzę sąsiadów, w których wyznaczam z jakiego pola, z jakim obróceniem, mogę gdzie pójść
# Następnie tworzę tyle pól odległości i visited
# Następnie uruchamiam dijkstrę i zwracam minimalny wynik


from colosses.egz2021t1.zad2testy import runtests
from queue import PriorityQueue


# face - w którą stronę patrzy robot
# 0 -> prawo
# 1 -> dół
# 2 -> lewo
# 3 -> góra

def get_neigh2(i, j, L, face):  # n to ->, m to \/
    neigh = []
    # print(i, j)
    n = len(L[0])
    m = len(L)

    if face == 2 and m > j - 1 >= 0:  # ruch w lewo legalny
        if L[i][j - 1] != "X":
            neigh.append((i, j - 1))
    if face == 3 and n > i - 1 >= 0:  # ruch w góre(i-1)
        if L[i - 1][j] != "X":
            neigh.append((i - 1, j))
    if face == 1 and 0 <= i + 1 < m:  # ruch w dół
        if L[i + 1][j] != "X":
            neigh.append((i + 1, j))
    if face == 0 and 0 <= j + 1 < n:  # ruch w prawo
        if L[i][j + 1] != "X":
            neigh.append((i, j + 1))
    return neigh


def robot(L, A, B):
    # zmiana współrzędnych A i B dla wygody
    n = len(L)
    m = len(L[0])
    NEIGH = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            NEIGH[i][j] = [0] * 4
    for i in range(n):
        for j in range(m):
            if L[i][j] != "X":
                for f in range(4):
                    NEIGH[i][j][f] = get_neigh2(i, j, L, f)
    # NEIGH to tablica sasiadow
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            visited[i][j] = [[False] * 4 for _ in range(4)]
    d = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            d[i][j] = [[float('inf')] * 4 for _ in range(4)]

    # kolejka postaci (pozycja, state, ostatnia predkosc)
    # opis state:
    # 0 -> patrzy prawo
    # 1 -> patrzy dół
    # 2 -> patrzy lewo
    # 3 -> patrzy góra
    # last predkosc:
    # 0 -> 0
    # 1 -> 60
    # 2 -> 40
    # 3 -> 30

    A2 = (A[1], A[0])
    B2 = (B[1], B[0])
    istart, jstart = A2
    idest, jdest = B2
    #       POS I,   POS J, FACING, LAST VELOCITY
    d[istart][jstart][0][0] = 0
    Q = PriorityQueue()
    # (d[i][j],  i ,  j,  f,  v)
    Q.put((d[istart][jstart][0][0], istart, jstart, 0, 0))

    while not Q.empty():
        c, i, j, f, v = Q.get()
        # print(c, i, j)
        if visited[i][j][f][v]:
            continue
        for e in NEIGH[i][j][f]:  # mozliwosci pojscia do przodu w kierunku patrzenia
            # print(e)
            i2, j2 = e
            if v == 0:
                w = 60
            elif v == 1:
                w = 40
            elif v == 2:
                w = 30
            else:
                w = 30
            # print("w:", w, "to:", i2, j2)
            if d[i2][j2][f][min(v + 1, 3)] > d[i][j][f][v] + w:
                d[i2][j2][f][min(v + 1, 3)] = min(d[i][j][f][v] + w, d[i2][j2][f][min(v + 1, 3)])
            Q.put((d[i2][j2][f][min(v + 1, 3)], i2, j2, f, min(v + 1, 3)))
        dir1, dir2 = -1, -1
        if f == 0 or f == 2:
            dir1 = 3
            dir2 = 1
        elif f == 1 or f == 3:
            dir1 = 0
            dir2 = 2
        # print("obroc:", c, i, j, dir, 0)
        if d[i][j][dir1][0] > d[i][j][f][v] + 45:
            d[i][j][dir1][0] = min(d[i][j][f][v] + 45, d[i][j][dir1][0])
        Q.put((d[i][j][dir1][0], i, j, dir1, 0))
        if d[i][j][dir2][0] > d[i][j][f][v] + 45:
            d[i][j][dir2][0] = min(d[i][j][f][v] + 45, d[i][j][dir2][0])
        Q.put((d[i][j][dir1][0], i, j, dir1, 0))
        Q.put((d[i][j][dir2][0], i, j, dir2, 0))
        visited[i][j][f][v] = True
    res = float('inf')
    for k in range(4):
        for l in range(4):
            # print(d[idest][jdest][k][l])
            if d[idest][jdest][k][l] < res:
                res = d[idest][jdest][k][l]
    return res if res !=float('inf') else None


def relax(d, u, v, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w


runtests(robot)
