"""
quicksort
"""

def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i] # swap
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort(A, p, r): #worst case logn space on stack
    while p<r:
        q = partition(A, p, r)

        if q - p < r - q:
            quicksort(A, p, q-1)
            p = q+1
        else:
            quicksort(A, q+1, r)
            r = q-1

def quicksortdefault(A, p, r): #with some optimalization
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        p = q + 1

def qs_iter(tab):
    stack = []
    stack.append((0, len(tab) - 1))

    while len(stack) > 0:
        p, r = stack.pop()
        if p < r:
            q = partition(tab, p, r)
            stack.append((p, q-1))
            stack.append((q+1, r))

def partitionH(A, p, r):
    pivot = A[p]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while (A[i] < pivot):
            i += 1
        j -= 1
        while (A[j] > pivot):
            j -= 1
        if (i >= j):
            return j
        A[i], A[j] = A[j], A[i]

def qsH(A, p, r):
    while p < r:
        q = partitionH(A, p, r)

        if q - p < r - q:
            quicksort(A, p, q )
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q

if __name__ == '__main__':
    A = [3,5,7,9,2,4,6,8]
    quicksort(A,4,len(A)-1)
    print(A)