# algorytm kruskala

class Node:
    def __init__(self):
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal_mst(L):  # [v1,v2,w]
    L.sort(key=lambda x: x[2])
    maxid = -1
    for e in L:  # O(E)
        maxid = max(maxid, e[0], e[1])
    n = maxid + 1
    A = []
    G = [Node() for _ in range(n)]
    for i in range(len(L)):
        u = L[i][0]
        v = L[i][1]
        if find(G[u]) != find(G[v]):
            A.append([u, v])
            union(G[u], G[v])
    return A


if __name__ == '__main__':
    L = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [0, 3, 1]]
    print(kruskal_mst(L))
