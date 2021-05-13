"""
radixsort string
sortowanie pozycyjne
Complexity O(d*n)
gdzie: d - ilość znaków w każdym słowie
       n - liczba słów
"""


def SortOnPosString(A, pos):  # sortuje A, ktora jest 2-wym, pos to index wg którego sortujemy
    n = len(A)
    dig = [0] * (58)  # 26 liter małych i 26 liter wielkich

    for i in range(0, n):
        dig[ord(A[i][pos]) - ord('A')] += 1  # zliczamy daną cyfrę
    for i in range(1, 58):  # część z countsorta, liczę ile na każdej pozycji jest wartości mniejszych
        dig[i] += dig[i - 1]

    res = [0] * n

    for i in range(n - 1, -1, -1):
        dig[ord(A[i][pos]) - ord('A')] -= 1
        res[dig[ord(A[i][pos]) - ord('A')]] = A[i]  # przepisuję do res

    for i in range(n):  # przepisuję wartosci do A
        A[i] = res[i]


def radixsortstring(A):  # moze sortowac podtablice ze stringami róznych dlugosci
    max_len = len(A[0])

    for i in range(max_len - 1, -1, -1):
        SortOnPosString(A, i)


if __name__ == '__main__':
    C = ["abz", "abc", "ABC"]
    radixsortstring(C)
    print(C)
