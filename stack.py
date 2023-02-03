"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO)
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""

stack = []

# implementation via list - simple
class Stack:
    def __init__(self):
        stack = []
    def empty():
        return not stack
    def size():
        return len(stack)
    def top():
        return stack[-1]
    def push(item):
        return stack.append(item)
    def pop():
      if not stack:
        return None
      return stack.pop()

if __name__ == '__main__':
    s = Stack
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

