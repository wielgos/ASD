class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.parent = None
        self.visited = None
        self.entry = None
        self.process = None

    def __repr__(self):
        return f"GraphNode[adj{self.adj}, parent{self.parent}, visited{self.visited}, entry{self.entry}, process{self.process}]"


def DFS(G):
    def DFSvisit(G, u):
        nonlocal time
        time += 1

        visited[u] = True
        entry[u] = time

        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                DFSvisit(G, v)

        time += 1
        process[u] = time

    n = len(G)
    visited = [False] * n
    parent = [-1] * n
    entry = [-1] * n
    process = [-1] * n
    time = 0

    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(G, u)

    return visited, parent, entry


def createadjmatrix(L):  # stworz macierz sąsiedztwa bazując na liscie krawedzi
    n = -1
    for i in range(len(L)):
        n = max(L[i][0], L[i][1], n)
    n += 1

    M = [[0] * n for _ in range(n)]
    for i in range(len(L)):
        M[L[i][0]][L[i][1]] = 1
    return M


if __name__ == "__main__":
    L = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 4), (2, 5), (3, 0), (3, 5), (3, 4), (4, 1), (4, 2), (4, 3),
         (5, 2), (5, 3)]
    # L to lista krawędzi

    G = createadjmatrix(L)
    v, p, e = DFS(G)
    print(v)
    print(p)
    print(e)
