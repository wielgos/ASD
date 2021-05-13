"""
minmax
"""


def minmax(l):
    # rozpatruję pierwsze elementy żeby miec co porownywac dalej

    if l[0] >= l[1]:
        min_l = l[1]
        max_l = l[0]
    else:
        max_l = l[1]
        min_l = l[0]

    for x in range(2, len(l), 2):
        if l[x] >= l[x + 1]:
            if min_l > l[x + 1]:
                min_l = l[x + 1]
            if max_l < l[x]:
                max_l = l[x]
        else:
            if min_l > l[x]:
                min_l = l[x]
            if max_l < l[x + 1]:
                max_l = l[x + 1]
    return min_l, max_l


def getmax(A):
    max = A[0]
    for i in range(1, len(A)):
        if A[i] > max:
            max = A[i]
    return max


if __name__ == '__main__':
    pass
