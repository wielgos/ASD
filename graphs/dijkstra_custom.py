from collections import deque


# E LOG V  -> TRUE VERSION

class MinHeap:  # [key, value]
    def __init__(self, length=0):
        self.elements = []
        self.size = 0
        self.H = [-1] * length
        self.idx = 0

    def b_down(self, i):  # O(logn)
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < self.size and self.elements[l][0] < self.elements[m][0]:
            m = l
        if r < self.size and self.elements[r][0] < self.elements[m][0]:
            m = r
        if m != i:
            self.elements[i][0], self.elements[m][0] = self.elements[m][0], self.elements[i][0]
            self.H[i], self.H[m] = self.H[m], self.H[i]
            self.b_down(m)

    def b_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.elements[i][0] < self.elements[parent][0]:
            self.elements[i][0], self.elements[parent][0] = self.elements[parent][0], self.elements[i][0]
            self.H[i], self.H[parent] = self.H[parent], self.H[i]
            self.b_up(parent)

    def put(self, v):  # append + O(log n)
        self.elements.append(v)
        self.size += 1
        self.H[self.idx] = self.size - 1
        self.idx += 1
        self.b_up(self.size - 1)

    def pop(self):
        result = self.elements[0][1]
        self.elements[0] = self.elements[self.size - 1]
        self.b_down(0)
        self.size -= 1
        return result

    def change_key(self, idx, key):
        if key < self.elements[self.H[idx]][0]:
            self.elements[self.H[idx]][0] = key
            self.b_up(self.H[idx])
        else:
            self.elements[self.H[idx]][0] = key
            self.b_down(self.H[idx])


def dijkstra(G, s):  # G to macierz sąsiedztwa
    def relax(u, v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    d = [float('inf')] * n
    parent = [None] * n
    d[s] = 0
    minh = MinHeap(n)
    for i in range(n):
        minh.put([float('inf'), i])

    while minh.size != 0:
        u = minh.pop()
        for v in range(n):
            if G[u][v] > 0:
                relax(u, v)
                minh.change_key(v, d[v])
    return d, parent


def pathrec(parent, s):
    if s is not None:
        pathrec(parent, parent[s])
        print(s, end=" ")


def path(parent, s):
    path = deque()
    len = 0
    while s is not None:
        path.append(s)
        s = parent[s]
        len += 1
    pathL = [0] * len
    for i in range(len):
        pathL[i] = path.pop()
    return pathL


if __name__ == '__main__':
    G = [[0, 10, 0, 0, 0, 0, 1],
         [10, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0]]

    G2 = [[0, 2, 4],
          [2, 0, 1],
          [4, 1, 0]]
    d, p = dijkstra(G, 0)
    print(d)
    print(p)
    print(path(p, 1))
