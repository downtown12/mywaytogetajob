class Solution(object):
        def uniquePathsWithObstacles(self, obstacleGrid):
                """
                :type obstacleGrid: List[List[int]]
                :rtype: int
                """
                m = len(obstacleGrid)
                if m<=0:
                   return 0
                n = len(obstacleGrid[0])

                #extreme condition
                if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
                        return 0

                #f(x, y): number of unique paths from position (x,y) to the down-right corner position (m-1,n-1)
                f = [[0]*(n+1) for i in range(m+1)]
                # initialize number of paths of right node to the the End Point(m-1,n-1) with 1.
                # so it can make sure f[m-1][n-1] == 1
                f[m-1][n] = 1

                #traversing and building the f matrix.
                for i in range(m-1,-1,-1):
                        for j in range(n-1,-1,-1):
                                if obstacleGrid[i][j]:
                                        #current position has an obstacle
                                        f[i][j] = 0
                                else:
                                        f[i][j] = f[i+1][j] + f[i][j+1]

                return f[0][0]

s = Solution()
obstacleGrid = [[0]*3, [0,1,0],[0]*3]
print obstacleGrid
print s.uniquePathsWithObstacles(obstacleGrid)



