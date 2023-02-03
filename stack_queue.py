"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO)
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""

# Deque implementation
from queue import LifoQueue

# implementation via list - simple
# Deque are better data structure for stack because deque does not move data while list does.
class Stack_Q:
    stack = LifoQueue()
    def empty(self):
        return not self.stack
    def size(self):
        return len(self.stack)
    # def top(self):
    #    return self.stack[0]
    def push(self, item):
        return self.stack.put(item)
    def pop(self):
      if not self.stack:
        return None
      return self.stack.get()

if __name__ == '__main__':
    s = Stack_Q()
    if s.empty():
      print ("Stack is empty")
    s.push(5)
    s.push("a")
    if s.empty():
      print ("Stack is empty")
    else:
      print ("Stack is not empty")

  
    print (f"top element: {s.pop()}")
    print (f"top element: {s.pop()}")
    # If I pop again, program is getting stuck.
