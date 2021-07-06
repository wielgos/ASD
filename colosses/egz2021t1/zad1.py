# Mikołaj Wielgos
# Pomysł na algorytm:
# na początku zmieniam elementy w tablicy T na krotki postaci: (wartosć, indeks)
# teraz sortuję tablicę T w czasie nlogn używając mergesort (stabilne sortowanie)
# Wynikiem jest posortowana tablica T z zapisanymi jej oryginalnymi indeksami i zachowaną kolejnością
# zatem teraz liniowym przejściem wyliczam największe k (różnica indeksu oryginalnego i po posortowaniu)

from colosses.egz2021t1.zad1testy import runtests


def mergesort(T):
    def cut(T, p, q):  # funkcja pomocnicza, pocinacz tablicy od p do q włącznie
        res = []
        for i in range(p, q + 1):
            res += [T[i]]
        return res

    def mergesorthelper(T):
        n = len(T)
        if n > 1:  # dzielę na części dopóki nie zostanie jeden element
            mid = n // 2
            L = cut(T, 0, mid - 1)  # ucinam T by uzyskać lewą część
            R = cut(T, mid, n - 1)  # ucinam T by uzyskać prawą część

            mergesort(L)  # posortuj dla części L
            mergesort(R)  # posortuj dla części R

            i = j = k = 0  # i-iteruje po tablicy L, j-iteruje po tablicy R, k-iteruje po finalnej tablicy
            n1 = len(L)
            n2 = len(R)
            # składanie razem posortowanych list L i R
            while (i < n1 and j < n2):  # iteruję po L i R dopóki mogę porównywać elementy
                if L[i] < R[j]:  # porownanie krotek
                    T[k] = L[i]
                    i += 1
                else:
                    T[k] = R[j]
                    j += 1
                k += 1
            if i == n1:  # sprawdzam z której tablicy mam przepisać pozostałe elementy
                for l in range(j, n2):
                    T[k] = R[l]
                    k += 1
            else:
                for l in range(i, n1):
                    T[k] = L[l]
                    k += 1

    mergesorthelper(T)  # sortuję mergesortem
    return T  # zwracam finalną posortowaną tablicę


def chaos_index(T):
    for i in range(len(T)):
        T[i] = (T[i], i)
    # print(T)
    mergesort(T)  # sortowanie jest stabilne (WAŻNE !!!)
    # print(T)
    # tablica T jest posortowana i mam jej krotki w postaci (wartosc, indeks)
    k = -1
    for i in range(len(T)):
        k = max(k, abs(i - T[i][1]))  # liczę wartość k
    return k


runtests(chaos_index)
