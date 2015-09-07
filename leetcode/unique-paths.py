# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # initialize the state matrix
        f = [[1] * n for i in range(m)]
### no need to do this, for the every element in the matrix f are initialized with 1.
#        # set every position that can be reached to the ENDPOINT horizontally and straightly to 1.
#        for i in range(n):
#                f[m*(n-2) + i] = 1
#        # set every position that can be reached to the ENDPOINT vertically and straightly to 1.
#        for i in range(m-1):
#                f[(n-1)*(m-i)] = 1

        for i in range(m-2,-1,-1):
                for j in range(n-2,-1,-1):
                    #f[x, y] = f[x+1, y] + f[x, y+1] 
                    #that is: f[cur_pos] = f[down_pos] + f[right_pos]
                     f[i][j] = f[i+1][j] + f[i][j+1]
        return f[0][0]


s = Solution()
import sys
m,n = sys.argv[1], sys.argv[2]
m,n = int(m), int(n)
print s.uniquePaths(m,n)
