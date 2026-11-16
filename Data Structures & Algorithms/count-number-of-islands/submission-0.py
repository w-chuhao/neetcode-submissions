class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1":
                    count+=1
                    self.dfs(row,col,grid)
        return count


    def dfs(self,row,col,grid):
        directions = [
            [-1,0],
            [1,0],
            [0,1],
            [0,-1]
        ]

        stack = [[row,col]]
        visited = set()
        grid[row][col] = "0"

        while stack:
            r,c = stack.pop()

            for dx,dy in directions:
                nr = r+dx
                nc = c+dy

                if (0<=nc<self.cols and 0<=nr<self.rows and grid[nr][nc]=="1"):
                    grid[nr][nc] = "0"
                    stack.append([nr,nc])
