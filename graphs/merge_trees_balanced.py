from queue import PriorityQueue


class BSTNode:
    def __init__(self, key=0):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def successor(node):
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


def predecessor(node):
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


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def delete(root, key):
    node = find(root, key)
    if node is None:
        return root

    if node.left is None and node.right is None:
        if node.parent is None:
            return None  # jedyny element w drzewie został usuniety
        if node.key < node.parent.key:
            node.parent.left = None
        else:
            node.parent.right = None
    elif node.left is not None and node.right is None: # nie ma lewego ale ma prawy
        if node.parent is None:
            node.left.parent = None
            return node.left  # nasz nowy root
        if node.key > node.parent.key:
            node.parent.right = node.left
            node.left.parent = node.parent
        else:
            node.parent.left = node.left
            node.left.parent = node.parent
    elif node.left is None and node.right is not None: # ma lewy ale nie ma prawego
        if node.parent is None:
            node.right.parent = None
            return node.right
        if node.key > node.parent.key:
            node.parent.right = node.right
            node.right.parent = node.parent
        else:
            node.parent.left = node.right
            node.right.parent = node.parent
    else:
        # szukamy następnika i wstawiamy w miejsce node'a
        nast = node.right
        flag = False
        while nast.left is not None:
            flag = True
            nast = nast.left

        if flag:
            nast.parent.left = None
        nast.left = node.left
        nast.parent = node.parent
        if node.parent is not None:
            if node.key > node.parent.key:
                node.parent.right = nast
            else:
                node.parent.left = nast
        else:
            return nast
    return root


def printall(root):
    if root is not None:
        print(root.key)
        printall(root.left)
        printall(root.right)


def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.key, end=" ")
        inOrderTraversal(root.right)


def insert(root, key):
    prev = None
    sroot = root
    while root is not None:
        prev = root
        if key > root.key:
            root = root.right
        elif key < root.key:
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


def tree_build(A, i, j, parent):  # buduje drzewo bazujac na medianach, tablica A jest posortowana
    if (j >= i):
        m = (i + j) // 2
        A[m].parent = parent
        A[m].left = tree_build(A, i, m - 1, A[m])
        A[m].right = tree_build(A, m + 1, j, A[m])
        return A[m]
    return None


def merge_trees(tab):
    Q = PriorityQueue()
    for e in tab:
        e = get_min_node(e)
        while e is not None:  # dodaje do kolejki wszystkei elementy w drzewie
            Q.put(e.key)
            e = successor(e)
    L = []
    prevkey = None
    while not Q.empty():  # zbieram wartosci z drzewa unikalne!!
        key = Q.get()
        if prevkey != key:
            L.append(BSTNode(key))
        prevkey = key
    return tree_build(L, 0, len(L) - 1, None)


if __name__ == "__main__":

    tr1 = None
    tr2 = None
    for i in range(100):
        tr1 = insert(tr1, i)
        tr2 = insert(tr2, i)

    inOrderTraversal(tr1)
    print()
    inOrderTraversal(tr2)
    print()
    tab = [tr1, tr2]
