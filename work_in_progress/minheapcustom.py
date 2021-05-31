# custom minheap where u can change the priorities
# but u cant pop and then add elements
# u can just firstly add elements, then swap their priorities, pop, change prio, and never add again
# so it mostly works in dijkstra

class MinHeap:  # [value, key]
    def __init__(self):
        self.elements = []
        self.size = 0
        self.H = []
        self.idx = 0

    def b_down(self, i):  # O(logn)
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < self.size and self.elements[l][1] < self.elements[m][1]:
            m = l
        if r < self.size and self.elements[r][1] < self.elements[m][1]:
            m = r
        if m != i:
            hr_i = self.elements[i][2]
            hr_m = self.elements[m][2]
            self.elements[i], self.elements[m] = self.elements[m], self.elements[i]
            self.H[hr_i], self.H[hr_m] = self.H[hr_m], self.H[hr_i]
            self.b_down(m)

    def b_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.elements[i][0] < self.elements[parent][0]:
            hr_i = self.elements[i][2]
            hr_parent = self.elements[parent][2]
            self.elements[i], self.elements[parent] = self.elements[parent], self.elements[i]
            self.H[hr_i], self.H[hr_parent] = self.H[hr_parent], self.H[hr_i]
            self.b_up(parent)

    def put(self, v):  # append + O(log n)
        self.elements.append(v + [self.idx])
        self.size += 1
        self.H.append(None)
        self.H[self.idx] = self.size - 1
        self.idx += 1
        self.b_up(self.size - 1)

    def pop(self):
        result = self.elements[0][0]
        self.elements[0] = self.elements[self.size - 1]
        h_0 = self.elements[0][2]
        h_l = self.elements[self.size - 1][2]
        self.H[h_0] = self.H[h_l]
        self.size -= 1
        self.b_down(0)
        return result

    def change_key(self, idx, key):
        if key < self.elements[self.H[idx]][1]:
            self.elements[self.H[idx]][1] = key
            self.b_up(self.H[idx])
        else:
            self.elements[self.H[idx]][1] = key
            self.b_down(self.H[idx])


# tests

minh = MinHeap()
minh.put([0, 1])
minh.put([1, 2])
minh.put([2, 3])
