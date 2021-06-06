# BST binarne drzewo przeszukiwan
# binary search tree


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


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
            root = root.right
        else:
            root = root.left
    new = BSTNode(key)
    if prev is None:
        return new
    new.parent = prev
    if key > prev.key:
        prev.right = new
    else:
        prev.left = new
    return sroot


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
    elif node.left is not None and node.right is None:
        if node.parent is None:
            node.left.parent = None
            return node.left  # nasz nowy root
        if node.key > node.parent.key:
            node.parent.right = node.left
            node.left.parent = node.parent
        else:
            node.parent.left = node.left
            node.left.parent = node.parent
    elif node.left is None and node.right is not None:
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


# root = BSTNode(14)
# root.left = BSTNode(2)
# root.left.parent = root
# root.right = BSTNode(17)
# root.right.parent = root
#
# root.left.left = BSTNode(1)
# root.left.right = BSTNode(3)
# root.left.left.parent = root.left
# root.left.right.parent = root.left
# root.left.left.left = BSTNode(0)
# root.left.left.left.parent = root.left.left
#
# root.right.right = BSTNode(19)
# root.right.right.parent = root.right
# root.right.right.left = BSTNode(18)
# root.right.right.left.parent = root.right.right
#
# root = delete(root, 14)
# print(root.key)
# print(root.left.key)
# print(root.right.key)
# print(root.left.right.key)
# root = delete(root, 3)
# print(root.left.right)
root = None
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 9)
root = insert(root, 8)
root = delete(root, 9)
while root is not None:
    print(root.key)
    root = root.right
