"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO)
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""

# implementation via list - linked list

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
    def __init__(self):
      self._stack = Node("head")
      self._size = 0

    def empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def top(self):
        if self.empty():
           return None
        return self._stack.next.value

    def push(self, item):
      n = Node(item)
      n.next = self._stack.next
      self._stack.next = n
      self._size += 1

    def pop(self):
      if self.empty():
        return None
      n = self._stack.next
      self._stack.next = self._stack.next.next
      self._size -= 1
      return n.value

if __name__ == '__main__':
    s = Stack()
    if s.empty():
      print ("Stack is empty")
    s.push(5)
    s.push("a")
    if s.empty():
      print ("Stack is empty")
    else:
      print ("Stack is not empty")

  
    print (f"top element: {s.top()}")
    print (f"top element: {s.top()}")
    print (f"top element: {s.pop()}")
    print (f"top element: {s.pop()}")
    print (f"top element: {s.pop()}")

