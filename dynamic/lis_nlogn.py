'''
Longest increasing subsequence
O(nlogn) using binary search
'''

def lis(A):
    n = len(A)
    P = [-1] * n #trzyma index poprzedniego elementu ciagu
    M = [0] * (n+1) #M[length_of_sequence] trzyma index k, taki ze A[k] jest koncowa wartoscia ciagu o dl length...
    # notatka: ciąg A[M[1]], A[[M[2]] ... jest rosnący (posortowany) więc mogę korzystać z bin_search

    L = 1
    M[1] = 0  #dla dlugosci=1 przyjmuje A[0] czyli M[1]=0 (indeks A[0])
    M[0] = -1 #nie ma LIS dla dlugosci=0

    for i in range(1,n):
        p = 1
        r = L
        while p <= r:
            mid = (p + r) // 2
            if (A[M[mid]] < A[i]):
                p = mid + 1
            else:
                r = mid - 1
        newL = p
        P[i] = M[newL - 1] #bo M[newL] to indeks ostatniego elementu ciagu dlugosci newL, a P trzyma poprzedni
        M[newL] = i
        if newL > L:
            L = newL#update max lis

    return P, M[L], L #previous_elements, last index of LIS, length of LIS

def printsolution(A, P, i):
    if i ==-1:
        return
    if i!=-1:
        printsolution(A, P, P[i])
    print(A[i], end=" ")

if __name__ == '__main__':
    A = [13, 7, 21, 42, 8, 2, 44, 53]
    P, index, length = lis(A)
    print(P, index, length)
    printsolution(A,P,index)
