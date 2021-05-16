from collections import deque


def bridges(G):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def DFSvisit(G, u):
        nonlocal letters
        nonlocal time
        time += 1
        entry[u] = time
        low[u] = time  # poki co najlepsze oszacowanie na low
        visited[u] = True
        kr_wst = deque()
        kid = deque()
        for v in range(len(G)):
            if G[u][v] == 1 and visited[v] and parent[u] != v:
                kr_wst.append(v)
            if G[u][v] == 1 and not visited[v]:
                kid.append(v)
                parent[v] = u
                DFSvisit(G, v)

        minentrywst = float('inf')
        while kr_wst:
            minentrywst = min(minentrywst, entry[kr_wst.pop()])
        minkid = float('inf')
        while kid:
            minkid = min(minkid, low[kid.pop()])

        low[u] = min(low[u], minentrywst, minkid)
        # print(f"vertex:{letters[u]},low:{low[u]},entry:{entry[u]},krws:{minentrywst},minkid:{minkid}")
        if entry[u] == low[u] and parent[u] != -1:
            found_bridges.append([u, parent[u]])

    n = len(G)
    visited = [False] * n
    entry = [-1] * n
    parent = [-1] * n
    low = [float('inf')] * n
    time = 0

    found_bridges = []
    # mostami będą entry[v]==low[v]

    for v in range(n):
        if not visited[v]:
            DFSvisit(G, v)

    return found_bridges


#     a  b  c  d  e  f  g  h
G = [[0, 1, 0, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 0],
     [1, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0]]
# graf spojny z wykladu
print(bridges(G))
