"""
mrege k arrays
"""


def merge(Left, Right):
    n1 = len(Left)
    n2 = len(Right)
    result = [0] * (n1 + n2)
    i = j = k = 0
    while i < n1 and j < n2:
        if Left[i] < Right[j]:
            result[k] = Left[i]
            i += 1
            k += 1
        else:
            result[k] = Right[j]
            j += 1
            k += 1
    if i == n1:
        for l in range(j, n2):
            result[k] = Right[l]
            k += 1
    else:
        for l in range(i, n1):
            result[k] = Left[l]
            k += 1
    return result


def merge_lists(lists):
    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                res = merge(lists[i], lists[i + 1])
            else:
                res = lists[i]
            new_lists.append(res)
        lists = new_lists
    return lists


if __name__ == '__main__':
    tab = [[1, 6, 11, 16, 21], [2, 7, 12, 17], [3, 8, 13, 18], [4, 9, 14, 19], [5, 10, 15, 20]]
    print(merge_lists(tab))
