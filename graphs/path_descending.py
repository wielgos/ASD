from collections import deque


def path_desc(G, s, t):
    def DFSvisit(G, u, last_w):
        nonlocal stop
        visited[u] = True

        for v, w in G[u]:
            if not visited[v] and w < last_w:
                parent[v] = u
                if v == t:
                    stop = True
                if stop:
                    return
                DFSvisit(G, v, w)

    stop = False
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    for u in range(len(G)):
        if not visited[u]:
            last_w = float('inf')
            DFSvisit(G, u, last_w)


    path = deque()
    length = 0
    while s != t:
        path.append(t)
        t = parent[t]
        length += 1

    path.append(s)
    length += 1
    pathL = [0] * length
    for i in range(length):
        pathL[i] = path.pop()
    return pathL


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

    print(path_desc(G3, 0, 3))
