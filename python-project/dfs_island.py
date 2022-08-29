class Graph:
    def __init__(self, row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph

    def dfs(self, i, j):
        rowNeighbour = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        colNeighbour = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
            return
        self.graph[i][j] = -1

        for visit in range(len(rowNeighbour)):
            self.dfs(i + rowNeighbour[visit], j + colNeighbour[visit])

    def countIslands(self):
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j] == 1:
                    self.dfs(i, j)
                    count += 1

        return count

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
        ]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print ("island number : ", g.countIslands())
