class Node:
    def __init__(self):
        self.cut = None  # klucz tego wezla
        self.left = None
        self.right = None
        self.intervals = []  # przedzialy
        self.lchild = None  # lewe dziecko
        self.rchild = None  # prawe dziecko
        self.leaf = False  # czy jest lisciem


def stworz_drzewo(A, i, j, left, right):
    X = Node()
    X.left = left
    X.right = right
    if j < i:
        X.cut = -1
        X.leaf = True
    else:
        m = (i + j) // 2
        X.cut = A[m]
        X.lchild = stworz_drzewo(A, i, m - 1, left, A[m])
        X.rchild = stworz_drzewo(A, m + 1, j, A[m], right)
    return X


def drzewo_przedzialowe(A):
    return stworz_drzewo(A, 0, len(A) - 1, min(A) - 1, max(A) + 1)


def przedzial_work(X, I, f):  # wykonuje prace na danym przedziale I  z funkcji f
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X, I)
        return
    if a < X.cut:
        przedzial_work(X.lchild, I, f)
    if b > X.cut:
        przedzial_work(X.rchild, I, f)


def przedzial_add(X, I):
    def insert(X, I):
        X.intervals.append(I)

    przedzial_work(X, I, insert)


def przedzial_remove(X, I):
    def remove(X, I):
        try:
            X.intervals.remove(I)
        except ValueError:
            pass

    przedzial_work(X, I, remove)


def przedzial_get(X, a):
    R = X.intervals.copy()
    if X.leaf:
        return R
    if a <= X.cut:
        R += przedzial_get(X.lchild, a)
    if a >= X.cut:
        R += przedzial_get(X.rchild, a)
    return R
