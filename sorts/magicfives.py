"""
magicfives
magiczne piatki

Algorytm nie tworzy dodatkowych tablic, natomiast wszystkie mediany 5-tek zamienia miejscami z pierwszymi elementami
tablicy. Następnie z tych pierwszych elementów tablicy (median) dalej wyliczam medianę i znów zamieniam miejscami,
przedział się zawęża, aż zostanę z 1 medianą median. Elementy w tablicy nie giną ponieważ je swapuję.
Z wyliczonej mediany, która zawsze jest na 1 indeksie danego przedziału [p,r], dokonuję partition całej tablicy
i dalej postępuję jak w algorytmie select.

* Jeżeli po dokonaniu partition, mój przedział zawęzi się do [q+1, r], to wtedy mediany umieszczam kolejno począwszy
od q+1, q+2 ...
"""


def partition(A, p,
              r):  # funkcja partition która za pivota bierze elemenet pod indeksem p, w tym miejscu zawsze znajdzie się mediana median
    i = p
    pivot = A[p]  # przyjmuję pivot jako A[p], gdzie na indeksie p leży mediana
    for j in range(p + 1, r + 1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap
    A[i], A[p] = A[p], A[i]
    return i


def insertionsort(T, p, r):  # insertion sort do sortowania piątek i niepełnych piątek
    i = p + 1
    while i <= r:
        j = i - 1
        while (j >= p and T[j] > T[j + 1]):
            T[j], T[j + 1] = T[j + 1], T[j]
            j -= 1
        i += 1


def createmed(T, p, r):  # funkcja rekurencyjna tworząca medianę median i umieszcza tę medianę ostatecznie na indeksie p
    count = p
    n = r - p + 1
    iter = n // 5
    if p < r:
        for i in range(
                iter):  # zbierz mediany z pełnych piątek i swapuj je z kolejnymi indeksami począwszy od p, p+1, ...
            insertionsort(T, p + i * 5, p + (i * 5) + 4)
            T[count], T[p + (i * 5) + 2] = T[p + (i * 5) + 2], T[count]
            count += 1
        if n % 5 != 0:  # zbierz medianę z niepełnych piątek i umieść na kolejnym wolnym p+k
            insertionsort(T, n - n % 5, n - 1)
            T[count], T[p + (n - iter * 5) // 2] = T[p + (n - iter * 5) // 2], T[count]
            count += 1
        if count != p + 1:  # jeżeli nie mam jednej mediany, liczę kolejną medianę z median już policzonych
            createmed(T, p, count - 1)


def magicfives(T, p, r, k):
    createmed(T, p, r)  # tworzę medianę median i ustawiam ją na indeksie p
    q = partition(T, p, r)  # układam elementy w tablicy względem pivota = mediany median
    if q == k:  # q jest na dobrym miejscu, więc jeżeli q==k to k-ty element to T[k]
        return T[k]
    elif k < q:  # q jest na dobrym miejscu, więc szukam w przedziale od p do q-1, tam będzie moja k-ta liczba
        return magicfives(T, p, q - 1, k)
    else:
        return magicfives(T, q + 1, r, k)  # odwrotnie


if __name__ == '__main__':
    T = [0, 7, 10, 6, 8, 5, 9, 2, 1, 4, 3]
    n = len(T) - 1
    print(magicfives(T, 0, 5, 5))
    print(T)
