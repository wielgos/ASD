'''
nie dziala as intended
nie dziala as intended
nie dziala as intended
nie dziala as intended
nie dziala as intended
nie dziala as intended
nie dziala as intended
'''

def tsp3(C):
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

    def tspf(i, j, F, D, R, flag=True):
        nonlocal C
        if F[i][j] != float('inf'):
            # R[j] = 0
            return F[i][j]
        if i == j - 1:  # przypadek (B) kiedy i == j-1
            best = float('inf')
            for k in range(j - 1):
                consider = tspf(k, j - 1, F, D, R, False) + D[k][j]
                if consider < best:
                    best_k = k
                    best = consider
            if flag:
                R[best_k] = "d"
            tspf(best_k, j - 1, F, D, R, True)
            F[i][j] = best
        else:  # przypadek (A) kiedy i < j-1
            if flag:
                R[j - 1] = "d"
                F[i][j] = tspf(i, j - 1, F, D, R, True) + D[j - 1][j]
            else:
                F[i][j] = tspf(i, j - 1, F, D, R, False) + D[j - 1][j]

        return F[i][j]

    def print_solution(C, R):
        print(C[0][0], end=", ")  # wypisz startowe miasto
        for i in range(1, len(R)):  # wypisujemy tylko te w prawo
            if R[i] == 'd':
                print(C[i][0], end=", ")
        print(C[len(R) - 1][0], end=", ")
        for i in range(len(R) - 2, 0, -1):  # wypisujemy tylko te w lewo
            if R[i] != 'd':
                print(C[i][0], end=", ")
        print(C[0][0])  # wypisz startowe miasto(końcowe)

    n = len(C)
    quicksort(C, 0, n - 1)
    D = set_distances(C)
    F = [[float('inf')] * n for _ in range(n)]
    F[0][1] = D[0][1]

    best = d(C[0], C[n - 1]) * (n + 1)

    for k in range(0, n - 2):
        R = [0] * n
        consider = tspf(k, n - 1, F, D, R) + D[k][n - 1]
        if consider < best:
            best = consider
            best_path = R

    print_solution(C, best_path)
    return best


if __name__ == '__main__':
    C1 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
    C2 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1], ["Papr", 1, 3], ["kox", 0.5, -2]]
    C3 = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2], ["Kraków", 2, 1], ["Papr", 7, 3], ["kox", 0.5, 4]]
    C4 = [["Wrocław", 0, 12], ["Warszawa", 1, 3], ["Gdańsk", 2, 8], ["Kraków", 12, -5], ["Papr", 4, -1], ["kox", 8, 9]]
    C5 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3],["F",0.5,-2]]
    C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
         ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
    print(tsp3(C))
