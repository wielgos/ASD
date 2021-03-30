"""
radixsort string
sortowanie pozycyjne
"""

def SortOnPos(A, pos, k):  # sortuje A, ktora jest 2-wym, pos to index, sortowanie countsort
    n = len(A)
    dig = [0] * (k+1)  # cyfry od 0 do 9

    for i in range(n):
        dig[A[i][pos]] += 1  # zliczamy daną cyfrę
    for i in range(1, k+1):  # część z countsorta
        dig[i] += dig[i - 1]

    res = [0] * n

    for i in range(n - 1, -1, -1):
        dig[A[i][pos]] -= 1
        res[dig[A[i][pos]]] = A[i]

    for i in range(n):  # przepisuję wartosci do A
        A[i] = res[i]
    # return res

def radixsort(A, k): #tablica A musi sie skladac z podtablic o rownej dlugosci
    max_len = len(A[0])
    for i in range(max_len-1, -1, -1):
        SortOnPos(A, i, k)

if __name__ == '__main__':
    A = [[1,3],[1,7],[1,9],[2,7],[1,2]]
    #OUTPUT: A = [[1, 2], [1, 3], [1, 7], [1, 9], [2, 7]]
    radixsort(A,10)
    print(A)