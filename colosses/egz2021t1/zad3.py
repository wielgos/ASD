# Mikołaj Wielgos
# Pomysł na algorytm
# Korzystam z F dynamicznej, gdzie F(i,j) = max mozliwy intersect z j przedziałów, konczacy sie w przedziale i
# w którym bedziemy również zapisywac dane przeciecie
# Niestety nie zdołałem dokonczyc zwracania wyniku, przez co algorytm nie zwraca dobrego wyniku

from colosses.egz2021t1.zad3testy import runtests


def przeciecie(I, X):  # przeciecie przedzialu I i przedzialu X
    a1, b1 = I
    a2, b2 = X
    b3 = min(b1, b2)
    a3 = max(a1, a2)
    return (a3, b3)


def kintersect(A, k):
    n = len(A)
    F = [[(0, 0)] * (k + 1) for _ in range(n)]
    m = [(A[i][0], i, A[i][1]) for i in range(n)]

    m.sort(key=lambda x: x[0])
    for i in range(n):
        F[i][0] = 0
        F[i][1] = (m[i][0], m[i][1])

    for i in range(n):
        for j in range(2, k + 1):
            for l in range(i):
                a, b = przeciecie(F[l][j - 1], A[i])
                if a >= b:
                    continue
                if b - a > F[i][j][1] - F[i][j][0]:
                    F[i][j] = a, b if b - a > F[i][j][1] - F[i][j][0] else F[i][j]
    # for i in range(n):
    #     print("Fik:", F[i][k])
    return list(range(k))


runtests(kintersect)
