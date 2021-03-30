"""
radixsort string
sortowanie pozycyjne
Complexity O(d*n)
gdzie: d - ilość znaków w każdym słowie
       n - liczba słów
"""

def SortOnPosString(A, pos):  # sortuje A, ktora jest 2-wym, pos to index wg którego sortujemy
    n = len(A)
    dig = [0] * (58)  # bo ord('z') - ord('A')=57 więc potrzebuję indeksy od 0 do 57

    for i in range(n):
        dig[ord(A[i][pos]) - ord('A')] += 1  # zliczamy daną cyfrę
    for i in range(1, 58):  # część z countsorta, liczę ile na każdej pozycji jest wartości mniejszych
        dig[i] += dig[i - 1]

    res = [0] * n

    for i in range(n - 1, -1, -1):
        dig[ord(A[i][pos]) - ord('A')] -= 1
        res[dig[ord(A[i][pos]) - ord('A')]] = A[i] #przepisuję do res

    for i in range(n):  # przepisuję wartosci do A
        A[i] = res[i]

def radixsortstring(A): #moze sortowac podtablice ze stringami róznych dlugosci
    max_len = 1
    for i in range(len(A)):
        max_len = max(max_len,len(A[i])) #sprawdzam najdluzszy string

    buckets = [[] for _ in range(0, max_len+1)]

    for i in range(len(A)):
        buckets[len(A[i])].append(A[i])

    for i in range(1, max_len+1):
        for j in range(i, 0, -1):
            SortOnPosString(buckets[i], j-1) # w kazdym buckecie sortuję od ostatnich digits

    i = 0
    for e in buckets: # finalnie sklejam rezultat od bucketów w których były elementy najkrótsze
        for e2 in e:
            A[i] = e2 #przepisuję wynik do tablicy A
            i += 1

if __name__ == '__main__':
    C = ["abc","def","aaa", "AXD","zzA"]
    radixsortstring(C)
    print(C)