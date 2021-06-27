class bst_node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        ret = ""
        if self.left:
            ret += str(self.left) + "<"
        ret += str(self.key)
        if self.right:
            ret += "<" + str(self.right)
        return ret

def insert(root,key) -> bst_node:
    # prosze uzupelnic implementacje
    return bst_node(key)

def suma(T,x,y) -> float:
    # prosze uzupelnic implementacje
    pass















# testy:
T = [-1.0,-2.0,-1.1,10.0,9.0,9.5,0.5,10.5,10.2,5.0]
root = None
for elem in T:
    root = insert(root,elem)

print(suma(root,-2.0,-1.0),"?=?",-4.1)
root = insert(root,-1.5)
print(suma(root,-2.0,-1.0),"?=?",-5.6)

print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5)
root = insert(root,6.7)
print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5 + 6.7)
inf = float('inf')
print(suma(T,-inf,inf),"?=?",55.8)

