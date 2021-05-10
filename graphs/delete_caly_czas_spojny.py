from collections import deque


class GraphNode:
    def __init__(self):
        self.neigh = deque()
        self.visited = 0
        self.process = -1

    def __repr__(self):
        return f"GraphNode[v{self.visited}, p{self.process}]"


def DFS(G):
    def DFSvisit(V, u):
        V[u].visited = 1

        while V[u].neigh:
            v = V[u].neigh.pop()
            if not V[v].visited:
                V[v].parent = u
                DFSvisit(V, v)
        order.append(u)

    order = deque()
    n = len(G)
    V = [GraphNode() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                V[i].neigh.append(j)

    for i in range(n):
        if not V[i].visited:
            DFSvisit(V, i)
    while order:
        print(order.popleft(), end=" ")


#      0  1  2  3  4
G1 = [[0, 1, 0, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 1, 0, 1, 0],
      [1, 0, 1, 0, 1],
      [0, 0, 0, 1, 0]]

G2 = [[0, 1, 0, 1, 0],
      [1, 0, 1, 0, 0],
      [0, 1, 0, 0, 0],
      [1, 0, 0, 0, 1],
      [0, 0, 0, 1, 0]]

G3 = [[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1],
      [0, 0, 0, 1, 0]]


DFS(G3)
