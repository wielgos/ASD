"""
bucketsort O(n)
sortujemy n liczb pochodzących z
!!!!rozkładu jednostajnego!!!! nad [0,1)

tworzymy zawsze n kubełków (lub mniej jezeli chcemy
oszczedzic pamiec)

x element wkladamy w floor(x*n) | lub n=k jezeli k kubelkow

jezeli chcemy normalizowac to dzielimy przez najwiekszy element wystepujacy
w tablicy wszystkie liczby, wtedy mamy [0,1]
"""


def insertionsort(T, p, r):  # insertion sort potrzebny do posortowania elementow w poszczegolnych kubelkach
    i = p + 1
    while i <= r:
        j = i - 1
        while (j >= p and T[j] > T[j + 1]):
            T[j], T[j + 1] = T[j + 1], T[j]
            j -= 1
        i += 1


def bucketsort(T, n):
    b = [[] for _ in range(n)]  # tworzę n kubełków

    # MAX = 10

    for i in range(len(T)):
        b[int(n * T[i])].append(T[i])  # dodaję elementy do odpowiedniego kubełka
        # b[int((n-1) * T[i] /MAX)].append(T[i])  #gdybym chcial normalizowac elementy, dziele przez MAX
    res = []
    i = 0
    for t in b:
        insertionsort(t, 0, len(t) - 1)  # sortuję elementy w danym kubełku
        for e in t:
            T[i] = e  # przepisuję posortowane elementy do T
            i += 1


if __name__ == '__main__':
    T = [0.1, 0.25, 0.2, 0.3, 0.11, 0.14, 0.6, 0.7, 0.3, 0.4, 0.85]
    bucketsort(T, len(T))
    print(T)
