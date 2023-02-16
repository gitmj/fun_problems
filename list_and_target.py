num = [2,7,11,15]
target = 18

# n2
for i, val1 in enumerate(num):
  for j, val2 in enumerate(num):
    if val1 + val2 == target:
      print ('found')
      print (f'index: {i} {j}')

# trick - only one pass
# keep track of values as you go through the list.
# compare target - val in the map (which are stored in list) ==> if zero then match
# if not then continue to store value.
#

check = {} # Will store key as 'num' of original list and index in the value part
# Idea is that this dictionary will remember what we passed through and their index
# Then at each pass, 
#     if target - val is equal to the value we already passed then BINGO, return index of (target-val) from check and current i
for i, val in enumerate(num):
  print (i, val)
  print (check)
  if target - val in check: # checking 
     print ([check[target - val], i])
  else:
    check[num[i]] = i
