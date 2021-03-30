from random import randint, seed
from time import time


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def arr_to_list(arr):
    list_head = None
    list_tail = None
    for value in arr:
        if list_head is None:
            list_head = Node(value)
            list_tail = list_head
            continue
        list_tail.next = Node(value)
        list_tail = list_tail.next

    return list_head


def print_list(list):
    tmp = list
    while tmp is not None:
        print(tmp.value, end=" ", sep=" ")
        tmp = tmp.next
    print("")


def merge_lists(l1, l2):
    new_list = Node(0)
    nl_head = new_list
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            new_list.next = l1
            l1 = l1.next
        else:
            new_list.next = l2
            l2 = l2.next
        new_list = new_list.next
    while l1 is not None:
        new_list.next = l1
        new_list = new_list.next
        l1 = l1.next
    while l2 is not None:
        new_list.next = l2
        new_list = new_list.next
        l2 = l2.next
    nl_head = nl_head.next
    return nl_head, new_list


# Funkcja znajdująca serię naturalną w liście jednokierunkowej
def find_sorted(l1):
    if l1 is None:
        return None, None
    series_head = l1
    series = l1
    l1 = l1.next
    while l1 is not None and l1.value >= series.value:
        series.next = l1
        series = series.next
        l1 = l1.next
    series.next = None
    return series_head, l1


# Funkcja sprawdzająca czy tablica została posortowana
def is_sorted(l1):
    p = l1
    q = l1.next
    while q is not None and p.value <= q.value:
        p = p.next
        q = q.next
    if q is None:
        return True
    return False


def merge_sort_list(l1):
    rest = l1  # część listy która jeszcze nie została sprawdzona w poszukiwaniu serii
    head = None
    curr = None
    while True:
        if rest is None:
            # Jeżeli cała lista została sprawdzona, sprawdź czy otrzymana lista jest posortowana
            if is_sorted(head):
                break
            rest = head
            head = None
        # Znajdź 2 kolejne serie naturalne
        m1, rest = find_sorted(rest)
        m2, rest = find_sorted(rest)

        # Ustal nagłówek połączonej listy, lub jeśli istnieje dopnij połączoną listę do istniejącej
        if head is None:
            head, curr = merge_lists(m1, m2)
        else:
            curr.next, curr = merge_lists(m1, m2)

    return head


start = time()
seed(42069)

lst = arr_to_list([randint(1, 10) for i in range(10)])
print_list(lst)
merge_sort_list(lst)
print(time() - start)
print_list(lst)



