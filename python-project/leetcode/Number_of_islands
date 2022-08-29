from cgitb import reset
from re import L


grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def dfs(i, j, grid):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == '0':
        return 
    grid[i][j] = "0"
    next_node = [ [i, j-1], [i, j+1], [i+1, j], [i-1, j] ]
    for node in next_node:
        dfs(node[0], node[1], grid)
    return 
def number_of_islands(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                res += 1
                dfs(i, j, grid)
    print(res)
    return res
if __name__ == '__main__':
    number_of_islands(grid1)
    number_of_islands(grid2)