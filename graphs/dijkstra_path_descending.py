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
    parent = [[] for _ in range(n)]
    pos = [0] * n
    d[s] = 0

    Q = PriorityQueue()
    Q.put((d[s], float('inf'), s))
    while not Q.empty():
        cur_d, last_w, u = Q.get()
        start_pos = pos[u]
        if u == t:
            print(f"cur_d:{cur_d}, par:{parent}")
        for i in range(start_pos, len(G[u])):
            v, w = G[u][i]
            #print(f"v:{v} in u:{u}, w:{w}, last_w:{last_w}")
            if w < last_w:
                Q.put((cur_d + w, w, v))
                if d[v] > cur_d + w:
                    d[v] = cur_d + w
                parent[v].append(u)
                pos[u] = i + 1
            else:
                break


    print(f"PARENT:")
    for e in parent:
        print(e)
    print()
    path = []
    while t != s:
        path.insert(0, t)
        for i in range(0, len(parent[t])):
            if parent[t][i] is not None:
                t = parent[t][i]
                break
    path.insert(0, s)

    print()
    print(d)

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
    print(dijkstra_desc(G2, 0, 3))
