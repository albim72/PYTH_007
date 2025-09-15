class Node:
    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(node):
    if node is None:
        return

    inorder(node.left) #lewa gałąź
    print(node.value,end=" ") #korzeń
    inorder(node.right) #prawa gałąź

#test

root  = Node(10,Node(5,Node(2),Node(7)),Node(15,None,Node(18) ) )

inorder(root)


