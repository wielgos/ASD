def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] > pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def select(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[k]
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def stypendia(T, A, k):
    m = len(T)
    n = len(T[0])
    final_score = 0
    for i in range(m):
        best_score = select(T[i], 0, len(T[i]) - 1, n // 4)

        ocena_studentki = T[i][A]
        score = 10
        l = n // 4
        while ocena_studentki != best_score and l > 0:
            if ocena_studentki > best_score:
                score -= 1
                l -= 1
                best_score = select(T[i], 0, len(T[i]) - 1, l)
            else:
                score -= 1
                l += 1
                best_score = select(T[i], 0, len(T[i]) - 1, l)
        final_score += score
    print(final_score)
    if final_score >= k:
        return True
    return False
    # tu umieść swoją implementację


# wszerz -> wszystkie oceny z itego przedmiotu
# kolumna -> oceny danej uczennicy
# czy studentka A otrzyma stypendium z progiem k

T = [[5.0, 5.0, 3.75, 4.5, 4.3, 4.1, 3.9, 4.9, 3.6, 2.0, 2.0, 2.0],
     [5.0, 4.6, 4.9, 4.2, 3.7, 4.0, 3.8, 4.01, 3.6, 3.5, 3.4, 2.0],
     [5.0, 4.7, 3.0, 3.5, 2.8, 2.7, 2.5, 2.0, 2.3, 2.2, 2.1, 2.4]]

print(stypendia(T, 0, 18))
print(stypendia(T, 0, 21))
