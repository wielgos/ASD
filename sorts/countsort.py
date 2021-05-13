"""
countsort O(n + k)
sortuje tablicę rozmiaru n
zawierajaca liczby od 0 do k-1
czyli jezeli liczby mam np. od 3 do 17 to k=18 bo ost. index to 17
"""


def countsort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):  # zliczam poszczegolne liczby
        C[A[i]] += 1
    for i in range(1, k):  # zmieniam wartosci na "ile jest mniejszych badz rownych od tej liczby"
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):  # przepisuję w odpowiednie miejsce do B
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(n):  # przepisuję B do A
        A[i] = B[i]
    # return B


if __name__ == '__main__':
    A = [3, 5, 7, 9, 2, 4, 6, 8]
    countsort(A, 10)
    print(A)
