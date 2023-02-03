import stack

# no framework, just test the methods by running them.

def test_stack():
  s = stack.Stack;
  assert s.empty() == True
  s.push(5)
  assert s.empty() == False
  assert s.top() == 5
  assert s.size() == 1
  item = s.pop()
  assert item == 5
  assert s.empty() == True

if __name__ == "__main__":
    test_stack()
    print("Everything passed")
