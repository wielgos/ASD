"""
heap, heapsort
"""


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(A, n, i):  # O(logn) maxheapify
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r

    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


def buildheap(A):  # O(nlogn)
    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heapsort(A):  # O(nlogn)
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def add_to_heap(A, v):  # append + O(log n)
    A.append(v)
    n = len(A)
    i = n - 1
    p = parent(i)
    while p >= 0 and A[p] < A[i]:
        A[p], A[i] = A[i], A[p]
        i = p
        p = parent(p)


if __name__ == '__main__':
    A = []
    add_to_heap(A, 1)
    add_to_heap(A, 6)
    add_to_heap(A, 4)
    add_to_heap(A, 0)
    add_to_heap(A, 9)
    print(A)
