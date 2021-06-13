def moral(A):
    n = len(A)
    F = [float('-inf')] * n
    for i in range(n):
        F[i] = A[i]

    def f(F, n):
        for j in range(n):
            if j - 2 >= 0:
                F[j] = max(F[j], F[j - 2] + A[j], F[j - 1])
            elif j - 1 >= 0:
                F[j] = max(F[j], F[j - 1])

    f(F, n)
    return F


def items(F):
    n = len(F) - 1
    while n >= 0:

        if n >= 2 and F[n] == F[n - 2] + A[n]:
            print(n)
            n = n - 2
        elif F[n] == F[n - 1]:
            print(n - 1)
            n -= 3
        elif F[n] - A[n] == 0:
            print(n)
            return
        else:
            n = n - 1


#    0  1  2  3  4  5
A = [1, 100, 3, 4, 100, 6]
F = moral(A)
print(F)
items(F)
