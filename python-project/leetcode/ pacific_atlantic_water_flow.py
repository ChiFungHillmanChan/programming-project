heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
def dfs(i, j, visited, n, m):
    MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    visited.add((i, j))
    for di, dj in MOVES:
        x, y = i + di, j + dj
        if 0 <= x < n and 0 <= y < m and (x, y) not in visited and heights[i][j] <= heights[x][y]:
            dfs(x, y, visited)


def pacificAtlantic(self, heights):
    n, m = len(heights), len(heights[0])

    atl_visited = set()
    pas_visited = set()

    for i in range(n):
        dfs(i,     0, pas_visited, n, m)
        dfs(i, m - 1, atl_visited, n, m)

    for j in range(m):
        dfs(    0, j, pas_visited, n, m)
        dfs(n - 1, j, atl_visited, n, m)

    return atl_visited & pas_visited


if __name__ == '__main__':
    pacificAtlantic(heights)

