# importing "heapq" to implement heap queue
import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(li)
 
# printing created heap
print ("The created heap is : ",(list(li)))
heapq.heappush(li,8)
print ("The created heap is : ",(list(li)))
heapq.heappop(li)
print ("The created heap is : ",(list(li)))

class Node:
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

# Min heap is complete binary tree in which the value of each 
# internal node is smaller than or equal to the values in the childeren.


# It's implemented via array because it's more efficient and allows to maintain 
# the complete binary tree property.
# Possible to do it with Binary tree as well that will make it more complicated.

class BinHeap:
  def __init__(self):
    self.heapL = [0]
    self.currentSize = 0

  def minChild(self, i):
    if ((i * 2) + 1 > self.currentSize):
      return i * 2 # There is only one child
    else:
      if self.heapL[i * 2] < self.heapL[i * 2 + 1]: # compare childs
        return i * 2
      else:
        return i * 2 + 1

  def moveUp(self, i):
    while i // 2 > 0: # i // 2 gives idx of parent i.e. if not root
      if self.heapL[i] < self.heapL[i // 2]: # if parent is bigger then swap
        tmp = self.heapL[i // 2]
        self.heapL[i // 2] = self.heapL[i]
        self.heapL[i] = tmp
      i = i // 2 # Move up to parent

  def moveDown(self, i):
    while (i * 2) <= self.currentSize:
      mc_idx = self.minChild(i)
      if self.heapL[i] < self.heapL[mc_idx]: # if parent is bigger then swap
        tmp = self.heapL[mc_idx]
        self.heapL[mc_idx] = self.heapL[i]
        self.heapL[i] = tmp
      i = mc_idx # move down to the min child idx

  def insert(self, val):
    self.heapL.append(val)
    self.currentSize += 1
    self.moveUp(self.currentSize)

  def delete(self):
    ret_val = self.heapL[1]
    self.heapL[1] = self.heapL[self.currentSize]
    self.currentSize -= 1
    self.heapL.pop()
    self.moveDown(1)
    return ret_val

  def print(self):
    print("heap: ", (list(self.heapL)))


H = BinHeap()
"""
H.insert(3)
H.insert(2)
H.insert(20)
H.insert(1)
"""
H.insert(5)
H.insert(7)
H.insert(9)
H.insert(1)
H.insert(3)
H.print()
print("min val: ", H.delete())
H.print()
print("min val: ", H.delete())
H.print()

