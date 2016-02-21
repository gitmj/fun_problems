# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

def printTree(tree):
        if tree != None:
            print(tree.getNodeValue())
            printTree(tree.getLeftChild())
            printTree(tree.getRightChild())



# test tree

def main():
    myTree = BinaryTree(1)
    myTree.insertLeft(2)
    myTree.insertRight(3)
    myTree.insertRight(5)
    printTree(myTree)

    # my code here

if __name__ == "__main__":
    main()
