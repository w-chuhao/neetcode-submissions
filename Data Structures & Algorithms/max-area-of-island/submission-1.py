class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0

        self.rows = len(grid)
        self.cols = len(grid[0])

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    self.dfs(row,col,grid)
        return self.max_area
    
    def dfs(self,row,col,grid):

        stack = [[row,col]]
        area = 1
        
        directions = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]

        while stack:
            r,c = stack.pop()

            for dx,dy in directions:
                nr = r+dx
                nc = c+dy

                if 0<=nr<self.rows and 0<=nc<self.cols and grid[nr][nc] == 1:
                    area+=1
                    grid[nr][nc] = 0
                    stack.append([nr,nc])
        self.max_area = max(area,self.max_area)

        