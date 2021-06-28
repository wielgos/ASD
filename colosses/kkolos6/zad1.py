class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.right = right
        self.left = left

def maxi_suma_pionowa(root):
    pass


root = Node(1)
root.left = Node(2)
root.right = Node(3,Node(5,Node(7),Node(8)),Node(6))
print(maxi_suma_pionowa(root),"?=?",11,",",6)

root = Node(-10,
        Node(-20,
            None,
            Node(-11)),
        Node(100,
            Node(90,
                Node(5,
                    None,
                    Node(50)),
                Node(95)),
            Node(105,
                Node(102),
                None)))
print(maxi_suma_pionowa(root),"?=?",195,",",-15)
