from collections import deque


def islands(G, A, B):
    # a start
    # b dest
    # min cost
    n = len(G)

    n = len(G)

    Q = deque()
    visited = [[False] * 9 for _ in range(n)]
    # 0 -> 1$
    # 1 -> 5$
    # 2 -> 8$
    d = [[float('inf')] * 9 for _ in range(n)]
    parent = [[-1] * 9 for _ in range(n)]
    d[A][1] = 0
    d[A][5] = 0
    d[A][8] = 0
    visited[A][1] = True
    visited[A][5] = True
    visited[A][8] = True
    Q.append((A, 1))
    Q.append((A, 5))
    Q.append((A, 8))
    # end -> ktorym dojechalem na wypse
    while Q:  # if deque is not empty
        u, end = Q.pop()
        if u == B:
            continue
        #$print(u, end)
        for v in range(n):
            if G[u][v] != 0 and G[u][v] != end:
                # jade do V
                # srodek to G[u][v]
                if not visited[v][G[u][v]]:
                    visited[v][G[u][v]] = True
                    d[v][G[u][v]] = d[u][end] + G[u][v]
                    parent[v] = u
                    Q.append((v, G[u][v]))
    return min(d[B])


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

print(islands(G2, 2, 0))
