class node:
    def __init__(self, v, next=None):
        self.v = v
        self.next = next


def linsert(head, v):
    if head is None or v < head.v:
        new_head = node(v, head)
        return new_head

    p = head
    while (p.next is not None and p.next.v < v):
        p = p.next
    new = node(v, p.next)
    p.next = new
    return head


def remove_max(head):  # DO CHECKED
    p = head
    q = None
    to_rm = None
    maximum = head.v
    while p is not None:
        if p.v > maximum:
            maximum = p.v
            to_rm = q
        q = p
        p = p.next
    if to_rm is None:
        head = head.next
    else:
        to_rm.next = to_rm.next.next
    return head, maximum


def lselect_sort(head):
    sorted_list = None
    while head is not None:
        head, m = remove_max(head)
        sorted_list = node(m, sorted_list)
    return sorted_list


if __name__ == '__main__':
    numbers = [8, 19, 11, 4, 21, 22, 7]
    list_head = None
    for x in numbers:
        list_head = node(x, list_head)
    list_head = lselect_sort(list_head)
    print("selection sort:")
    l = list_head
    while l is not None:
        print(l.v)
        l = l.next
