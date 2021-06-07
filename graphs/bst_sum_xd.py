class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.down = 0



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


root = None
root = insert(root, 5)
root = insert(root, 4)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 1)


def sumbst(root):
    if root is None:
        return 0
    return root.key + sumbst(root.left) + sumbst(root.right)

print(sum(root))

