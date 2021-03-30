"""
select
wyznacza element, ktory po posortowaniu tablicy
znalazlby sie na indeksie k-tym
k=0 minimum
k=n-1 maksimum
"""
def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i] #swap
    A[i+1], A[r] = A[r], A[i+1]
    return i+1 #zwracam indeks

def select(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[k]
    elif k < q:
        return select(A, p, q-1, k)
    else:
        return select(A, q+1, r, k)

if __name__ == '__main__':
    A = [8,5,7,6,4, 9,2,1,0,3]
    print(select(A,0,len(A)-1,4))