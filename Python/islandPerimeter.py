class Solution(object):
    def islandPerimeter(self, grid):
        rows=len(grid)
        column=len(grid[0])
        zero_matrix = [[0 for col in range(column+2)] for row in range(rows+2)]
        for i in range(rows):
            for j in range(column):
                if grid[i][j]==1:
                    zero_matrix[i+1][j+1]=1
        print(zero_matrix)
        count=0
        for i in range(rows+2):
            for j in range(column+2):
                if zero_matrix[i][j]==1:
                    for x in range(i-1,i+2):
                        if(zero_matrix[x][j]==0):
                            count+=1
                    for y in range(j-1,j+2):
                        if(zero_matrix[i][y]==-0):
                            count+=1                
        return count
