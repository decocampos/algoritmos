class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        self.lista=[]
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root=None

    def simetric_traversal (self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        self.lista.append(node.data)
        if node.right:
            self.simetric_traversal(node.right)

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else: 
            parent.right = Node(value)

books = input().split(" ")
tree = BinarySearchTree()

for book in books:
  tree.insert(int(book))
  
tree.simetric_traversal()
print(" ".join(map(str, tree.lista)))
  
