from colosses.asdt0.zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane



def valuableTree(T, k):
    def countNodes(root):
        nonlocal cnt
        if root:
            countNodes(root.left)
            cnt += 1
            countNodes(root.right)
    def restructurize(root, cnt):
        if root:
            root.X = [float('inf')]*cnt
            countNodes(root.left)
            countNodes(root.right)
    cnt = 0
    countNodes(T)
    cnt += 1
    restructurize(T, cnt)

    return 0


runtests(valuableTree)
