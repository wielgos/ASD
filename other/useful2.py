class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def add_elements(t, first):
    for i in range(len(t) - 1, -1, -1):
        q = Node(t[i])
        first, q.next = q, first
    return first


def wypisz(p):
    while p is not None:
        print(p.value, end="")
        print(" → ", end="")
        p = p.next
    print("None")


def usun(first):  # funkcja usuwająca (zmienia wskaźniki), usuwa wszystkie zdarzenia, nie pojedyncze!
    w = Node(None, first)
    prev = w
    p = w.next
    while p is not None:
        deleted = False
        while p is not None and p.value==2:  # warunek usunięcia
            prev.next = p.next
            p = prev.next
            deleted=True
        if not deleted:
            prev, p = p, p.next
    return w.next

def add(first,value):
    return Node(value,first)

def add_on_end(first,value):
    w = Node(None,first)
    while w.next is not None:
        w = w.next
    w.next = Node(value,None)
    return first

def usun2(first):  # funkcja usuwająca (zmienia wskaźniki) pierwszy napotkany element usuwa
    w = Node(None, first)
    prev = w
    p = w.next
    while p is not None:
        if p.value == 2:  # warunek usunięcia
            prev.next = p.next
            p = p.next
        else:
            prev, p = p, p.next
    return w.next


first = add_elements([4,2,2,2,2,4],None)
wypisz(first)
first = add_on_end(first,10)
wypisz(first)