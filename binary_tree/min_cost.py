import random
from collections import deque

import queue


class BinaryTree():

    def __init__(self,data):
      self.left = None
      self.right = None
      self.data = data 
      self.cost = 0

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.data = value
    def getNodeValue(self):
        return self.data

    def insertRight(self, value):
        if self.right == None:
            self.right = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.right = self.right
            self.right = tree

    # Index is seq position in BFS order
    # Insert zero value nodes if path is missing.
    def insertAtIndex(self,index, value):
      q = queue.Queue()
      q.enqueue(self)
      trav_index = 0
      while q.isEmpty() != True:
        node = q.dequeue();
        trav_index = trav_index + 1

        
        if node.left == None:
          val = random.randint(1, 10) 
          node.left = BinaryTree(val)
        q.enqueue(node.left)

        if node.right == None:
          val = random.randint(1, 10) 
          node.right = BinaryTree(val)
        q.enqueue(node.right)

        if trav_index == index:
          node.data = value;
          return

    def insertLeft(self,value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.left = self.left
            self.left = tree

def printTree(tree):
        if tree != None:
            print(tree.getNodeValue())
            printTree(tree.getLeftChild())
            printTree(tree.getRightChild())

def printBFSTree(tree):
  q = queue.Queue()
  q.enqueue(tree)

  num_nodes_curr = 1
  num_nodes_next = 0
  while q.isEmpty() != True:
    node = q.dequeue();
    print node.data, node.cost
    num_nodes_curr = num_nodes_curr - 1

    if node.left != None:
      q.enqueue(node.left)
      num_nodes_next = num_nodes_next + 1

    if node.right != None:
      q.enqueue(node.right)
      num_nodes_next = num_nodes_next + 1

    if (num_nodes_curr == 0):
      print '####  Next Level ####'
      num_nodes_curr = num_nodes_next
      num_nodes_next = 0

def minCost(tree):
  if tree != None:
    minCost(tree.getLeftChild())
    minCost(tree.getRightChild())
    print 'min cost: ', tree.data
    if (tree.left == None and tree.right == None):
      tree.cost = tree.data
    if (tree.left == None and tree.right != None):
      tree.cost = tree.data  + tree.right.data
    elif (tree.left != None and tree.right == None):
      tree.cost = tree.data  + tree.left.data
    elif (tree.left != None and tree.right != None):
      if tree.left.data < tree.right.data:
        tree.cost = tree.data  + tree.left.data
      else:
        tree.cost = tree.data  + tree.right.data

def printMinPath(tree):
  if (tree == None):
    return None
  print tree.data
  if (tree.left != None and tree.right != None):
    if tree.left.cost < tree.right.cost:
      printMinPath(tree.left)
    else:
      printMinPath(tree.right)

  if (tree.left == None):
    return printMinPath(tree.right)

  if (tree.right == None):
    return printMinPath(tree.left)

  return None

def main():
   myTree = BinaryTree(1)
   myTree.insertLeft(6)
   myTree.insertLeft(2)
   myTree.insertRight(5)
   myTree.insertRight(3)

   myTree.insertAtIndex(4, 4)
   myTree.insertAtIndex(5, 5)
   myTree.insertAtIndex(7, 5)
   printBFSTree(myTree)

   minCost(myTree)
   print 'Next ######################################'
   printBFSTree(myTree)

   print 'Path ######################################'
   printMinPath(myTree)


if __name__ == "__main__":
    main()
