class Node:
    def __init__(self):
        self.cut = None  # klucz tego wezla
        self.left = None
        self.right = None
        self.intervals = []  # przedzialy
        self.lchild = None  # lewe dziecko
        self.rchild = None  # prawe dziecko
        self.leaf = False  # czy jest lisciem
        self.height = 0


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


def calc_h(X):
    if X.leaf:
        return 0
    if X is not None:
        return X.height + calc_h(X.lchild) + calc_h(X.rchild)


def przedzial_work(X, I, f):  # wykonuje prace na danym przedziale I  z funkcji f
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X, I)
        return
    if a < X.cut:
        przedzial_work(X.lchild, I, f)
    if b > X.cut:
        przedzial_work(X.rchild, I, f)


def get_height(X, I):  # wykonuje prace na danym przedziale
    (a, b) = I
    if a <= X.left and b >= X.right:
        return X.height + calc_h(X)
    if a < X.cut:
        return get_height(X.lchild, I)
    if b > X.cut:
        return get_height(X.rchild, I)


def przedzial_add(X, I, h):
    def insert(X, I):
        X.intervals.append(I)
        X.height = h
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


from queue import PriorityQueue


def block_height(K):
    Q = PriorityQueue()
    for i in range(len(K)):
        Q.put(K[i][0])
        Q.put(K[i][1])
    K2 = []
    while not Q.empty():
        K2.append(Q.get())
    X = drzewo_przedzialowe(K2)
    for e in K:
        (a, b, h) = e
        przedzial_add(X, (a, b), h)
    max_height = 0
    for e in K:
        (a, b, h) = e
        I = (a, b)
        height = get_height(X, I)
        print(height, I)
        max_height = max(max_height, height)
    return max_height


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


K1 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R1 = 6

K2 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R2 = 5

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
