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

def radixsort(A, k): #moze sortowac podtablice o roznej dlugosci
    max_len = 1
    for i in range(len(A)):
        max_len = max(max_len,len(A[i]))

    buckets = [[] for _ in range(0, max_len+1)]

    for i in range(len(A)):
        buckets[len(A[i])].append(A[i])

    for i in range(1, max_len+1):
        for j in range(i, 0, -1):
            SortOnPos(buckets[i], j-1, k) # w kazdym buckecie sortuję od ostatnich digits

    i = 0
    for e in buckets: # finalnie sklejam rezultat od bucketów w których były elementy najkrótsze
        for e2 in e:
            A[i] = e2 #przepisuję wynik do tablicy A
            i += 1
    # return res

if __name__ == '__main__':
    A = [[1,3],[1,7,9],[1,4,9],[2,7],[1,2]]
    #OUTPUT: A = [[1, 2], [1, 3], [2, 7], [1, 4, 9], [1, 7, 9]]
    radixsort(A,10)
    print(A)