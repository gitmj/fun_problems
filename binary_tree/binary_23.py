"""
Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties −

One node is marked as Root node.

Every node other than the root is associated with one parent node.

Each node can have an arbiatry number of chid node.
"""

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def insert(self, value):
    """
    1. If value is bigger than Node, go right. If empty, add Node.
    2. if value is smaller than Node, go left. If empty, add Node.
    3. if value is same as Node, overwrite and return.
    """ 
    if value > self.value:
      if self.right is None:
        self.right = Node(value)
      else:
        #Insert on right node. 
        self.right.insert(value)

    if value < self.value:
      if self.left == None:
        self.left = Node(value)
      else:
        self.left.insert(value)

  def _find_smallest(self, node):
    if node.left != None:
      self._find_smallest(node.left)
    return node

  def delete(self, value):
    """
    Go for in-order travesal so that if delete node is found, we can work on previous node.
    1. If value is bigger than Node, go right. If empty, not found.
    2. if value is smaller than Node, go left. If empty, not found.
    3. if value is same as Node, found. Delete the node.
      - if no left, no right, then easy removal. Return.
      - if no right, then move up the left and connect with rest of the tree.
      - if no left, then move up the right and connect with rest of the tree.
      - if both left and right present, then pick one and connect to the parent.

    """ 
    if not self:
      return self

    if value > self.value:
      if self.right is None:
        return self
      else:
        # find on right side. 
        # if node found then self.right would act like a parent and get adjusted.
        self.right = self.right.delete(value)

    if value < self.value:
      if self.left == None:
        return self
      else:
        # find on left side.
        # if node found then self.left would act like a parent and get adjusted.
        self.left = self.left.delete(value)

    if value == self.value:
        
      if self.left == None:
        return self.right
      if self.right == None:
        return self.left

      # find the smallest in the right hand side of tree
      smallest_node = self._find_smallest(self.right)
      self.value = smallest_node.value
      self.right = self.right.delete(self.value)
    return self
    
  #Pre-order print
  def print(self):
    print(self.value)
    if self.left:
      self.left.print()
    if self.right:
      self.right.print()




root = Node(10)
root.insert(20)
root.insert(5)
root.insert(25)
root.insert(15)
print("new")
root.print()
root.delete(2)
print("new")
root.print()
root.delete(20)
print("new")
root.print()
