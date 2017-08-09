
# tree is a tuple (node value, list_of_subtrees) 
def longest_path(tree): 
  value = tree[0] 
  subtrees = tree[1] 

  # length of longest consecutive path with root. 
  with_root = 1 
  # length of longest consecutive path without root. 
  without_root = 0 

  for subtree in subtrees: 
    s_value = subtree[0] 
    s_with_root, s_without_root = longest_path(subtree) 

    without_root = max(without_root, s_with_root, s_without_root) 

    # the root and the child are consecutive. 
    if s_value == value + 1: 
      with_root = max(with_root, s_with_root + 1) 

  return with_root, without_root 


def test(): 
  # 4->2->3->4->6 
  # ->2->2 
  tree = (4, [(2, [(3,[(4,[(6,[])])])]), (2, [(2,[])])]) 
  print max(longest_path(tree))

# only root
def only_root_test(): 
  tree = (4, [])
  print max(longest_path(tree))

def vector_test():
  tree = (4, [(1, [(3,[(4,[(6,[])])])])]) 
  print max(longest_path(tree))

if __name__ == "__main__":
  only_root_test()
  vector_test()
  test()
