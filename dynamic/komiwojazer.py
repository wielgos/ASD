'''
problem komiwojazera O(n^2)

'''

def tsp(C):
    def partition(A, p, r):
        pivot = A[r][1]
        i = p - 1
        for j in range(p, r):
            if A[j][1] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):  # worst case logn space on stack
        while p < r:
            q = partition(A, p, r)
            if q - p < r - q:
                quicksort(A, p, q - 1)
                p = q + 1
            else:
                quicksort(A, q + 1, r)
                r = q - 1

    def d(A, B):
        return ((B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2) ** (0.5)

    def set_distances(C):
        n = len(C)
        D = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                D[i][j] = d(C[i], C[j])
        return D

    def tspf(i, j, F, D):
        if F[i][j] != float('inf'):
            return F[i][j]
        if i == j - 1:  # przypadek (B) kiedy i == j-1
            best = float('inf')
            for k in range(j - 1):
                consider = tspf(k, j - 1, F, D) + D[k][j]
                if consider < best:
                    best = consider
            F[i][j] = best
        else:  # przypadek (A) kiedy i < j-1
            F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]
        return F[i][j]

    n = len(C)
    quicksort(C, 0, n - 1)
    D = set_distances(C)
    F = [[float('inf')] * n for _ in range(n)]
    F[0][1] = D[0][1]

    best = float('inf')

    for k in range(0, n - 2):
        consider = tspf(k, n - 1, F, D) + D[k][n - 1]
        if consider < best:
            best = consider
    return best


if __name__ == '__main__':
    C1 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
    C2 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Papr", 1, 3], ["kox", 0.5, -2]]
    C3 = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2], ["Kraków", 2, 1], ["Papr", 7, 3], ["kox", 0.5, 4]]
    C4 = [["Wrocław", 0, 12], ["Warszawa", 1, 3], ["Gdańsk", 2, 8], ["Kraków", 12, -5], ["Papr", 4, -1], ["kox", 8, 9]]
    C5 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3],["F",0.5,-2]]
    C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
         ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
    print(tsp(C))
