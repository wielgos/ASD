"""
binary search
posortowana tablica, O(log n)
"""

def bin_search(A, p, r, x): #zwraca indeks pod którym siedzi X (lub -1 jak nie istnieje)
    if p <= r:
        mid = (p+r)//2

        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return bin_search(A, p, mid -1, x)
        else:
            return bin_search(A, mid + 1, r, x)
    else:
        return -1

if __name__ == '__main__':
    A = [3,5,7,9,2,4,6,8]
    A.sort()
    print(A)
    print(bin_search(A,0,len(A)-1,6))