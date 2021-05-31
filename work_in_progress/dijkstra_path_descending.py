from queue import PriorityQueue


def dijkstra_desc(G, s, t):  # G to macierz sąsiedztwa
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    n = len(G)

    # sortowanie

    for i in range(n):
        G[i].sort(key=lambda x: x[1])

    d = [float('inf')] * n
    parent = [[None] * n for _ in range(n)]
    parentW = [[None] * n for _ in range(n)]
    pos = [0] * n
    d[s] = 0

    Q = PriorityQueue()
    Q.put((d[s], float('inf'), s))
    total_cost = None
    while not Q.empty():
        cur_d, last_w, u = Q.get()  # u to krawedz na ktorej skonczylismy
        start_pos = pos[u]
        for i in range(start_pos, len(G[u])):
            v, w = G[u][i]
            # print(f"cur_d:{cur_d},last_w:{last_w},u:{u}, v:{v}, w:{w}")
            if w < last_w:
                Q.put((cur_d + w, w, v))
                # if d[v] > cur_d + w:
                #     d[v] = cur_d + w
                parent[v][u] = u
                parentW[v][u] = w
                pos[u] = i + 1
            else:
                break
        if u == t:
            total_cost = cur_d
            break

    if total_cost is None:
        print("IMPOSSIBLE")
        return []

    # print(f"PARENT:")
    # for e in parent:
    #     print(e)
    # print()
    # print(f"PARENTW:")
    # for e in parentW:
    #     print(e)
    # print()

    path = []
    prev = -1
    while t != s:
        path.insert(0, t)
        for i in range(0, len(parent[t])):
            if parent[t][i] is not None and parentW[t][i] > prev:
                prev = parentW[t][i]
                t = parent[t][i]
                break
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
