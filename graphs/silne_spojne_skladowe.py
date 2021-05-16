def sss(G):
    def DFSvisit(G, u, reversed=False, index=-1):
        nonlocal time
        time += 1

        visited[u] = True
        if reversed:
            assigned[u] = index
        for v in range(len(G)):
            if reversed:
                if G[v][u] == 1 and not visited[v]:
                    DFSvisit(G, v, True, index)
            else:
                if G[u][v] == 1 and not visited[v]:
                    DFSvisit(G, v)

        time += 1
        process[u][0] = time

    n = len(G)
    visited = [False] * n
    process = [[-1, i] for i in range(n)]
    time = 0
    DFSvisit(G, 0)

    visited = [False] * n
    assigned = [-1] * n
    process.sort(key=lambda x: x[0], reverse=True)  # posortuj malejąco po 1 elemencie w sublistach
    num = 0
    for e in process:
        if not visited[e[1]]:
            DFSvisit(G, e[1], True, num)
            num += 1
    return assigned


G = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
# graf spojny z wykladu
print(sss(G))
