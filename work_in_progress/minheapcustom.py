# custom minheap where u can change the priorities

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
            self.elements[i], self.elements[m] = self.elements[m], self.elements[i]
            self.H[i], self.H[m] = self.H[m], self.H[i]
            self.b_down(m)

    def b_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.elements[i][0] < self.elements[parent][0]:
            self.elements[i], self.elements[parent] = self.elements[parent], self.elements[i]
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
        self.H[0] = self.H[self.size - 1]
        self.size -= 1

        self.b_down(0)
        return result

    def change_key(self, idx, key):
        if key < self.elements[self.H[idx]][0]:
            self.elements[self.H[idx]][0] = key
            self.b_up(self.H[idx])
        else:
            self.elements[self.H[idx]][0] = key
            self.b_down(self.H[idx])


# tests

minh = MinHeap(3)
minh.put([1, 1])
minh.put([2, 2])
minh.put([3, 3])

for i in range(3):
    print()
    print(minh.H)
    print(minh.elements)
    minh.change_key(i, 9-i)
    print(i)
    print(minh.elements)
    print(minh.H)
    print()

for i in range(3):
    print(minh.pop())
