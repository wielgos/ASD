from collections import deque


class GraphNode:
    def __init__(self):
        self.adj = deque()  # listy sąsiedztwa
        self.d = None
        self.visited = None
        self.parent = None

    def __repr__(self):
        return f"GraphNode[adj{self.adj}, d{self.d}, visited{self.visited}, parent{self.parent}]"


def BFS(G, s):  # G is a list of GraphNodes, s is starting vertex

    n = len(G)
    GR = [0] * n
    for i in range(n):
        v = GraphNode()
        v.visited = False
        v.d = -1
        v.parent = None

        for j in range(n):
            if G[i][j] == 1:
                v.adj.append(j)

        GR[i] = v

    Q = deque()
    GR[s].d = 0
    GR[s].visited = True
    Q.append(s)  # we put index of vertex, to get data we use G[s]
    while Q:  # if deque is not empty
        u = Q.pop()
        while GR[u].adj:
            v = GR[u].adj.pop()
            if not GR[v].visited:
                GR[v].visited = True
                GR[v].d = GR[u].d + 1
                GR[v].parent = u
                Q.append(v)


def createadjmatrix(L):  # stworz macierz sąsiedztwa bazując na liscie krawedzi
    n = -1
    for i in range(len(L)):
        n = max(L[i][0], L[i][1], n)
    n += 1

    M = [[0] * n for _ in range(n)]
    for i in range(len(L)):
        M[L[i][0]][L[i][1]] = 1
    return M


if __name__ == '__main__':
    L = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 4), (2, 5), (3, 0), (3, 5), (3, 4), (4, 1), (4, 2), (4, 3),
         (5, 2), (5, 3)]
    # L to lista krawędzi

    M = createadjmatrix(L)
    # M to reprezentacja macierzowa na podstawie listy krawędzi

    LADJ = [[1, 2, 3], [0, 4], [0, 4, 5], [0, 5, 4], [1, 2, 3], [2, 3]]
    # LADJ to listy sąsiedztwa
    print()
    BFS(M, 0)
