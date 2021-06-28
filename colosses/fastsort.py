from colosses.fastsorttesty import runtests
import math


# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała
# wieksza od 1 (a>1), x to liczby rzeczywiste rozlozone rownomiernie na przedziale [0,1]
# Napisz fast_sort, ktora przyjmuje talbice liczb z wynikami eksperymentu oraz stala a i zwraca tablice z wynikami
# eksperymentu posortowanymi rosnaco.

def insertionsort(T, p, r):  # insertion sort potrzebny do posortowania elementow w poszczegolnych kubelkach
    i = p + 1
    while i <= r:
        j = i - 1
        while (j >= p and T[j] > T[j + 1]):
            T[j], T[j + 1] = T[j + 1], T[j]
            j -= 1
        i += 1


def bucketsort(T, n, a):
    b = [[] for _ in range(n)]  # tworzę n kubełków

    for i in range(len(T)):
        value = math.log(T[i], a) #cala magia??
        b[int(n * value)].append(T[i])  # dodaję elementy do odpowiedniego kubełka
    res = []
    i = 0
    for t in b:
        insertionsort(t, 0, len(t) - 1)  # sortuję elementy w danym kubełku
        for e in t:
            T[i] = e  # przepisuję posortowane elementy do T
            i += 1


def fast_sort(tab, a):
    bucketsort(tab, len(tab), a)
    return tab


runtests(fast_sort)
