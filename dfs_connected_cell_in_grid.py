'''
https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

Consider a matrix with  rows and  columns, where each cell contains either a
or a  and any cell containing a  is called a filled cell. Two cells are said to
be connected if they are adjacent to each other horizontally, vertically, or
diagonally; in other words, cell  is connected to cells , , , , , , , and ,
provided that the location exists in the matrix for that .

If one or more filled cells are also connected, they form a region. Note that
each cell in a region is connected to at least one other cell in the region but
is not necessarily directly connected to all the other cells in the region.

Task 
Given an  matrix, find and print the number of cells in the largest region in
the matrix. Note that there may be more than one region in the matrix.

Input Format

The first line contains an integer, , denoting the number of rows in the
matrix. 
The second line contains an integer, , denoting the number of columns in the
matrix. 
Each line  of the  subsequent lines contains  space-separated integers
describing the respective values filling each row in the matrix.

Sample Input

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

Sample Output

5
'''

n = int(raw_input().strip())
m = int(raw_input().strip())

# grid = []
grid = [[0 for x in range(n)] for y in range(m)]
# for i in range(int(n)):
     
        
grid = [raw_input().split() for _ in range(int(n))]
    
# print grid

def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion
            
def countCells(grid, i, j):
    if (not(i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == '0'):
        return 0
    count = 1
    grid[i][j] = '0'
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count

print getBiggestRegion(grid)
