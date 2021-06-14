from queue import PriorityQueue


# BST binarne drzewo przeszukiwan
# binary search tree


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.remain = 1


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def insert(root, key):
    prev = None
    sroot = root
    while root is not None:
        prev = root
        if key > root.key:
            root.remain += 1
            root = root.right
        elif key < root.key:
            root.remain += 1
            root = root.left
        else:
            return sroot  # FALSE NOT INSERTED
    new = BSTNode(key)
    if prev is None:
        return new  # TRUE INSERTED SOME KEY
    new.parent = prev
    if key > prev.key:
        prev.right = new
    else:
        prev.left = new
    return sroot  # TRUE INSERTED SOME KEY


def fix_up(node):
    node.remain -= 1
    if node.parent is not None:
        fix_up(node.parent)


def remove(root, key):
    node = find(root, key)
    if node is None:
        return root
    if node.left is None and node.right is None:
        if node.parent is None:
            return None  # jedyny element w drzewie został usuniety
        if node.key < node.parent.key:
            node.parent.left = None
            fix_up(node.parent)
        else:
            node.parent.right = None
            fix_up(node.parent)
    elif node.left is not None and node.right is None:
        if node.parent is None:
            node.left.parent = None
            return node.left  # nasz nowy root
        if node.key > node.parent.key:
            node.parent.right = node.left
            node.left.parent = node.parent
            fix_up(node.parent)
        else:
            node.parent.left = node.left
            node.left.parent = node.parent
            fix_up(node.parent)
    elif node.left is None and node.right is not None:
        if node.parent is None:
            node.right.parent = None
            return node.right
        if node.key > node.parent.key:
            node.parent.right = node.right
            node.right.parent = node.parent
            fix_up(node.parent)
        else:
            node.parent.left = node.right
            node.right.parent = node.parent
            fix_up(node.parent)
    else:
        # szukamy następnika i wstawiamy w miejsce node'a
        nast = node.right
        flag = False
        while nast.left is not None:
            flag = True
            nast = nast.left
        if flag:
            nast.parent.left = None
        fix_up(nast.parent)
        nast.left = node.left
        nast.remain = node.remain
        nast.parent = node.parent
        nast.right = node.right
        if node.parent is not None:
            if node.key > node.parent.key:
                node.parent.right = nast
            else:
                node.parent.left = nast
        else:
            return nast
    return root


def getNext(node):  # następnik danego node'a
    if node.right is not None:  # idziemy prawo i max lewo
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    tmp = node.parent
    while tmp is not None and tmp.left is not node:
        node = tmp
        tmp = tmp.parent
    return tmp


def getPrev(node):  # poprzednik danego node'a
    if node.left is not None:  # idziemy na lewo i max prawo
        node = node.left
        while node.right is not None:
            node = node.right
        return node
    tmp = node.parent
    while tmp is not None and tmp.right is not node:
        node = tmp
        tmp = tmp.parent
    return tmp


def get_min_node(root):
    while root.left is not None:
        root = root.left
    return root


def get_max_node(root):
    while root.right is not None:
        root = root.right
    return root


def tree_build(A, i, j, parent):  # buduje drzewo na medianach, tablica A jest posortowana, drzewo jest zbalansowane
    if (j >= i):  # A to tablica node'ów
        m = (i + j) // 2  # obliczam indeks mediany przedziału
        A[m].parent = parent  # danemu elementowi przypisuję parenta
        A[m].left = tree_build(A, i, m - 1, A[m])  # wyznaczam jego lewe poddrzewo
        A[m].right = tree_build(A, m + 1, j, A[m])  # wyznaczam jego prawe poddrzewo
        return A[m]
    return None


def merge_trees(tab):  # k-trees O(nk*logk)
    Q = PriorityQueue()
    k = len(tab)

    for i in range(k):
        if tab[i] is not None:
            tab[i] = get_min_node(tab[i])
            Q.put((tab[i].key, tab[i]))
    L = []
    while not Q.empty():
        key, node = Q.get()
        if len(L) > 0 and L[-1] == key:
            node = getNext(node)
            if node is not None:
                Q.put((node.key, node))
        else:
            L.append(BSTNode(node.key))
            node = getNext(node)
            if node is not None:
                Q.put((node.key, node))
    return tree_build(L, 0, len(L) - 1, None)


def get_remain(node):
    return 0 if node is None else node.remain


def k_elem(node, k):
    if k == get_remain(node.left) + 1:
        return node
    elif k <= get_remain(node.left):
        return k_elem(node.left, k)
    elif k > get_remain(node) - get_remain(node.right):
        return k_elem(node.right, k - get_remain(node.left) - 1)


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.remain, end=" "),
        printInorder(root.right)


# r1 = None
# r2 = None
# r3 = None
# r4 = None
#
# for i in range(10):
#     r1 = insert(r1, i)
#     r2 = insert(r2, i + 10)
#     r3 = insert(r3, i + 20)
#     r4 = insert(r4, i + 30)

r1 = None
r1 = insert(r1, 10)
r1 = insert(r1, 5)
r1 = insert(r1, 4)
r1 = insert(r1, 7)
r1 = insert(r1, 6)
r1 = insert(r1, 8)
printInorder(r1)
r1 = remove(r1, 5)
print()
printInorder(r1)
print()
for i in range(1, 6):
    print(k_elem(r1, i).key)
