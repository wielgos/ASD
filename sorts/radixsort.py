"""
radixsort
sortowanie pozycyjne O(d*n)
gdzie d - digits
      n - numbers
sortujemy od najmniej znaczacych cyfr/wartosci
"""


def getmax(A):
    max = A[0]
    for i in range(1, len(A)):
        if A[i] > max:
            max = A[i]
    return max


def SortOnPos(A, pos):  # sortuje A wedlug danej pozycji (pos=1,10,100...) przez countsort
    n = len(A)
    dig = [0] * 10  # bo cyfr mamy 10 - 0,1,2,3,4,5,6,7,8,9

    for i in range(n):
        id = A[i] // pos  # ucinam liczbę, by na %10 mieć cyfrę z danego pos (pos=1,10,100...)
        dig[id % 10] += 1  # zliczamy daną cyfrę
    for i in range(1, 10):  # część z countsorta
        dig[i] += dig[
            i - 1]  # liczę na danej pozycji ile liczb jest mniejszych lub równych, by potem znać dokładne pozycje

    res = [0] * n

    for i in range(n - 1, -1, -1):
        id = A[i] // pos  # ucinam liczbę
        dig[id % 10] -= 1
        res[dig[id % 10]] = A[i]

    for i in range(n):  # przepisuję wartosci do A
        A[i] = res[i]
    # return res


def radixsort(A):
    maxv = getmax(A)
    pos = 1  # zaczynam od pierwszej cyfry

    while maxv > 0:
        SortOnPos(A, pos)
        maxv = maxv // pos
        pos = pos * 10


if __name__ == '__main__':
    A = [43, 232, 131, 1, 323, 434322]
    radixsort(A)
    print(A)
