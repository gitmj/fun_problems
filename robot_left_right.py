"""
Robot can go only right and down and it  needs to reach the bottom right in
grid of r rows and c coloumns. It's possible that some grids are offlimit.
Find a path to reach bottom right.
"""
from datetime import datetime

grid = [] 
grid.append([])
grid[0].append(0)
grid[0].append(0)
grid[0].append(0)
grid.append([])
grid[1].append(1)
grid[1].append(1)
grid[1].append(0)
grid.append([])
grid[2].append(0)
grid[2].append(1)
grid[2].append(0)

MAX_R = 2
MAX_C = 2
def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print grid[i][j]

"""
1. Keep going deep on column.
2. Once max column then go back one column and incr row and again max col.
3. Once max row and max col, final.
4. if not go back one more col and incr row and again max col.
"""
d = False
def find_path(r, c, done):
    global d
    p = []
    if d == True:
        return []
    if (r == MAX_R) and (c == MAX_C):
        d = True
        return [(r, c)]
    if grid[r][c] == 1:
        # blocked
        return []
    if (r <= MAX_R and c < MAX_C):
        p = p + find_path(r, c + 1, False)
    if (r < MAX_R and c <= MAX_C):
        p = p + find_path(r + 1, c, False)
    p = p + [(r,c)]
    if done == True:
        print 'final', p
    return p

"""
Starting from target and moving towards origin.
"""
def book_sol(grid, r, c, path):
    #print r, c
    #print grid[r][c]
    if r < 0 or c < 0 or grid[r][c] == 1:
        return False

    isOrigin = False
    if r == 0 and c == 0:
        isOrigin = True
    if (isOrigin == True or book_sol(grid, r, c - 1, path)
        or book_sol(grid, r - 1, c, path)):
        path.append((r, c))
        return True
    return False        
                                                                     
def book_sol_mem(grid, r, c, path, failed):
    # print grid[r][c]
    if r < 0 or c < 0 or grid[r][c] == 1:
        return False
    if (r, c) in failed:
        print 'f:', r, c
        return False

    isOrigin = False
    if r == 0 and c == 0:
        isOrigin = True
    if (isOrigin == True or book_sol_mem(grid, r, c - 1, path, failed)
        or book_sol_mem(grid, r - 1, c, path, failed)):
        path.append((r, c))
        return True
    print r,c
    failed.add((r,c))
    return False        

if  __name__ == "__main__":
    # print_grid()
    find_path(0, 0, True)
    # Recursive approch Big O: 2 pow (r+c).
    path = []
    startTime = datetime.now()
    if book_sol(grid, len(grid) - 1, len(grid[0]) - 1, path) == True:
        print path
    else:
        print 'Not found'
    print datetime.now() - startTime 

    # Dynamic programming approch Big O: O(rc).
    failed = set()
    path1 = []
    startTime = datetime.now()
    if book_sol_mem(grid, len(grid) - 1, len(grid[0]) - 1, path1, failed) == True:
        print path1
    else:
        print 'Not found'
    print datetime.now() - startTime    
    ## In small matrix, cache does not get hit. Howeveer, timing of both
    # appraoches are different. Which ever function gets executed later, posts
    # smaller time. Perhaps, because data is loaded in memory but still weird.

