from queue import PriorityQueue

# jest mozliwa implementacja O( (V+E)*(dl_slowa) )

def letters(G, W):  # G to macierz sąsiedztwa

    n = len(G[1])
    L = G[0]
    E = G[1]
    H = [[] for _ in range(n)]
    for e in E:
        H[e[0]].append((e[1], e[2]))
        H[e[1]].append((e[0], e[2]))

    Q = PriorityQueue()
    mini = float('inf')
    for i in range(len(L)):
        if L[i] == W[0]:
            idx = 0
            Q.put((0, idx, i))
            while not Q.empty():
                s, idx, u = Q.get()
                # print(f"idx:{idx},u:{u}, L:{L[idx]}")
                if idx == len(W) - 1:
                    mini = min(s,mini)
                else:
                    for v, w in H[u]:
                        if (L[v] == W[idx + 1]):
                            # print(f"v:{v},w:{w}, L:{L[v]}")
                            Q.put((s + w, idx + 1, v))
    return mini if mini!=float('inf') else -1


if __name__ == '__main__':
    L = ["k", "k", "o", "o", "t", "t"]
    E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
    G = (L, E)
    print(letters(G, "ktotototo"))
