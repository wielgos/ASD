'''
Longest decreasing subsequence
O(n^2)
'''


def lds(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n  # to obtain result later
    maxF = 0
    indexF = -1
    for i in range(1, n):
        for j in range(0, i):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j  # to obtain result later
                if F[i] > maxF:
                    maxF = F[i]  # collect maximum value in F during the loop
                    indexF = i
    return maxF, indexF, P


def printsolution(A, P, i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i])


if __name__ == '__main__':
    A = [13, 7, 21, 42, 8, 2, 44, 53]
    maxF, indexF, P = lds(A)
    printsolution(A, P, indexF)
    pass
