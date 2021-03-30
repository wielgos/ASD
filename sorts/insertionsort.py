'''
insertion sort
'''

def insertionsort(T):
    i = 1
    n = len(T)
    while i < n:
        j = i - 1
        while (j >= 0 and T[j] > T[j + 1]):
            T[j], T[j + 1] = T[j + 1], T[j]
            j -= 1
        i += 1