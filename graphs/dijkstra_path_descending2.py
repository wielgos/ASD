from queue import PriorityQueue


class Edge:
    def __init__(self, dest, w, idx):
        self.dest = dest
        self.w = w
        self.idx = idx
        self.p = None


def dijkstra_desc(G, s, t):  # G to macierz sąsiedztwa
    n = len(G)
    pos = [0] * n
    E = []
    for i in range(n):
        G[i].sort(key=lambda x: x[1])

    idx = 0
    for i in range(n):
        for j in range(len(G[i])):
            E.append(Edge(G[i][j][0], G[i][j][1], idx))
            G[i][j] = idx  # krotka z krawedzia zawiera teraz numer krawedzi
            idx += 1

    Q = PriorityQueue()
    for i in G[s]:
        Q.put((E[i].w, E[i].idx))

    total_cost = None
    while not Q.empty():
        cur_cost, edge = Q.get()  # u to krawedz na ktorej skonczylismy
        u = E[edge].dest  # wierzcholek docelowy prowadzacy z krawędzi edge, na tym aktualnie stoimy
        start_pos = pos[u]
        for i in range(start_pos, len(G[u])):
            if E[G[u][pos[u]]].w < E[edge].w:  # kolejne krawedzie wychodzace z u, badamy warunek
                next = G[u][pos[u]]  # następny to będzie ta krawędź
                E[next].p = edge  # dla parenta następnego wpisujemy aktualną krawędź
                Q.put((cur_cost + E[next].w, next))  # dodajemy do kolejki
                pos[u] = i + 1  # przesuwamy tablice pozycji
            else:
                break
        if u == t:  # jezeli jestemy juz u celu
            last = edge
            total_cost = cur_cost
            break

    if total_cost is None:  # nie udalo nam sie dotrzec do celu
        print("IMPOSSIBLE")
        return []
    print(total_cost)
    path = []
    while last is not None:  # printowanie drogi
        path.insert(0, E[last].dest)
        last = E[last].p
    path.insert(0, s)
    return path


if __name__ == '__main__':
    G = [[(1, 6), (2, 2)],
         [(0, 6), (2, 4)],
         [(0, 2), (1, 4), (3, 3)],
         [(2, 3)]]
    G2 = [[(1, 6), (2, 9)],
          [(0, 6), (2, 4)],
          [(0, 9), (1, 4), (3, 3)],
          [(2, 3)]]
    G3 = [[(1, 6), (2, 9), (3, 1)],
          [(0, 6), (2, 4)],
          [(0, 9), (1, 4), (3, 3)],
          [(0, 1), (2, 3)]]
    G4 = [
        [[2, 100], [1, 4]],  # 0
        [[0, 4], [4, 3]],  # 1
        [[3, 200], [0, 100], [4, 4]],  # 2
        [[2, 200], [4, 3]],  # 3
        [[2, 4], [1, 3], [3, 3]]  # 4
    ]
    G5 = [[(1, 6), (2, 7), (3, 8), (4, 12)],
          [(0, 6), (3, 3)],
          [(0, 7), (4, 3)],
          [(1, 3), (0, 8), (4, 2), (5, 4)],
          [(0, 12), (2, 3), (3, 2), (5, 2)],
          [(3, 4), (4, 2)]]

    print(dijkstra_desc(G5, 0, 5))
