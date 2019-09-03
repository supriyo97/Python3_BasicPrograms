class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class bTree(Node):
    def __init__(self):
        self.root = None

    def insertChildNode(self):
        self.root = Node('2')
        self.root.left = Node('1')
        self.root.right = Node('3')
        #You can add more forward

    def display(self,traverse_type):
        if (traverse_type == "preorder"):
            return self.preorder(tree.root, "")
        elif (traverse_type == "postorder"):
            return self.postorder(tree.root, "")
        elif (traverse_type == "inorder"):
            return self.inorder(tree.root, "")
        else:
            print("Wrong Choice for now!!!")

    def preorder(self,start,traverse):         #root,left,right
        if start:
            traverse += (str(start.info) + " -> ")
            traverse = self.preorder(start.left,traverse)
            traverse = self.preorder(start.right,traverse)
        return traverse

    def postorder(self,start,traverse):        #left,right,root
        if start:
            traverse = self.preorder(start.left,traverse)
            traverse = self.preorder(start.right,traverse)
            traverse += (str(start.info) + " -> ")
        return traverse

    def inorder(self,start,traverse):          #left,root,right
        if start:
            traverse = self.preorder(start.left,traverse)
            traverse += (str(start.info) + " -> ")
            traverse = self.preorder(start.right,traverse)
        return traverse

tree = bTree()
tree.insertChildNode()
print(tree.display("preorder"))
print(tree.display("postorder"))
print(tree.display("inorder"))
