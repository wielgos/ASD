# Mikołaj Wielgos 29.03.2021
from colosses.zad3testy import runtests

'''
Algorytm wykorzystuje bucketsort do sortowania poszczególnych elementów
Najpierw wyszukuję przechodząc po T, maksymalną wartość  oraz najmniejszą O(n)
Używam jej do normalizowania wartosci.
Umieszam je w bucketach, a w bucketach uzywam insertion sort (z niską stałą)
Złożoność to złożoność algorytmu bucketsort
Używam n dodatkowej pamięci, do zapisywania w bucketach

'''


def SortTab(T, P):
    def insertionsort(T, p, r):  # insertion sort potrzebny do posortowania elementow w poszczegolnych kubelkach
        i = p + 1  # uzywam insertion ze wzgledu na niską stałą (mam bardzo malo elementow do posrotowania w kubelkach)
        while i <= r:
            j = i - 1
            while (j >= p and T[j] > T[j + 1]):
                T[j], T[j + 1] = T[j + 1], T[j]
                j -= 1
            i += 1

    def bucketsort(T, n, maxv, minv):
        b = [[] for _ in range(n)]  # tworzę n kubełków
        for i in range(len(T)):
            if T[i] == maxv:
                b[n - 1].append(T[i])
            b[int(n * (T[i] - minv) / (maxv - minv + 1))].append(T[i])  # normalizuje elementy
        i = 0
        for t in b:
            insertionsort(t, 0, len(t) - 1)  # sortuję elementy w danym kubełku
            for e in t:
                T[i] = e  # przepisuję posortowane elementy do T
                i += 1

    n = len(T)  # tyle ile jest liczb będziemy tworzyc kubelkow
    maxv = P[0][1]
    minv = P[0][0]
    for i in range(len(P)):
        if P[i][1] > maxv:
            maxv = P[i][1]  # znajduję maksymalną wartość którą może być w T
        if P[i][0] < minv:
            minv = P[i][0]
    bucketsort(T, n, maxv, minv)

    return


runtests(SortTab)
