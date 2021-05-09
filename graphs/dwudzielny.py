from collections import deque


class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []  # listy sąsiedztwa
        self.d = None

    def __repr__(self):
        return f"GraphNode[adj{self.adj}, d{self.d}]"


def dwudzielny_bfs(G, s):  # G is a list of GraphNodes, s is starting vertex
    Q = deque()
    if G[s].d == None:
        G[s].d = 0
    Q.append(s)  # we put index of vertex, to get data we use G[s]
    while Q:
        u = Q.pop()
        for v in G[u].adj:
            if G[u].d == 0:
                num = 1
            else:
                num = 0
            if G[v].d == None:
                G[v].d = num
                Q.append(v)
            elif G[v].d != num:
                return False
    return True


def dwudzielny(G):
    for i in range(len(G)):
        G[i].d = None

    for i in range(len(G)):
        if not dwudzielny_bfs(G, i):
            return False
    return True


if __name__ == '__main__':
    G = [
        GraphNode([3, 5, 4]),  # 0
        GraphNode([4]),  # 1
        GraphNode([5, 3, 4]),  # 2
        GraphNode([0, 2]),  # 3
        GraphNode([1, 0]),  # 4
        GraphNode([2, 0]),  # 5

        GraphNode([7]),  # 6
        GraphNode([6]),  # 7

        GraphNode([9]),  # 8
        GraphNode([10]),  # 9
        GraphNode([8])  # 10
    ]
    L = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 4), (2, 5), (3, 0), (3, 5), (3, 4), (4, 1), (4, 2), (4, 3),
         (5, 2), (5, 3)]
    print(dwudzielny(G))
    print(G)
