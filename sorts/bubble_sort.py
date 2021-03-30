def bubble_sort(t):
    for i in range(0, len(t) - 1):
        for j in range(0, len(t) - i - 1):
            if t[j] > t[j + 1]:
                t[j + 1], t[j] = t[j], t[j + 1]

if __name__ == '__main__':
    numbers = [8, 19, 11, 4, 21, 22, 7]
    bubble_sort(numbers)
    print(numbers)