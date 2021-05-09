

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

        G[u].visited = True
        G[u].entry = time

        for v in G[u].adj:
            if not G[v].visited:
                G[v].parent = u
                DFSvisit(G, v)

        time += 1
        G[u].process = time

    for v in range(len(G)):
        G[v].visited = False
        G[v].parent = None
        G[v].entry = None
        G[v].process = None

    time = 0

    for u in range(len(G)):
        if not G[u].visited:
            DFSvisit(G, u)


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
    G = [
        GraphNode([1, 2, 3]),  # 0
        GraphNode([0, 4]),  # 1
        GraphNode([0, 4, 5]),  # 2
        GraphNode([0, 5, 4]),  # 3
        GraphNode([1, 2, 3]),  # 4
        GraphNode([2, 3]),  # 5
    ]
    DFS(G)
    print(G)
