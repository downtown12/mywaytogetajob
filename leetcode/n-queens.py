'''
This solution refers to the bitmask way of this page:
    --> https://leetcode.com/discuss/35128/accepted-solution-use-backtracking-bitmask-easy-understand
In this solution, I use 3 boolean lists to store the valid-to-put-a-queen-flag of columns, the diagonals of downward-leftward direction and the diagonals of downward-rightward direction.
The 3 boolean lists are f_col, f_downkeft, and f_down_right

This solution costs only a half of time of the solution directly calculate if a position can be placed with a queen.
'''

class Solution:
    # @return a list of lists of string
    def __init__(self):
        self.sols = []
    
    def convertFormat(self,a_sol,n):
        res = []
        for i in range(n):
            a_line = '.'*a_sol[i] + 'Q' + '.'*(n-a_sol[i]-1)
            res.append(a_line)
        
        return res
    
    def putQueens(self, n, a_sol, f_col, f_downleft, f_downright, row):
        if row==n:
            a_res = self.convertFormat(a_sol, n)
            self.sols.append(a_res[:])
            return

        for col in range(n):
            if f_col[col] and f_downleft[row+col] and f_downright[n+row-col-1]:
                f_col[col] = f_downleft[row+col] = f_downright[n+row-col-1] = False
                a_sol[row] = col
                self.putQueens(n, a_sol, f_col, f_downleft, f_downright, row+1)
                f_col[col] = f_downleft[row+col] = f_downright[n+row-col-1] = True
                a_sol[row] = -1
        
    def solveNQueens(self, n):
        f_col = [True]*n
        f_downright = [True]*(2*n-1) # diagnose: \ 
        f_downleft = [True]*(2*n-1)# diagnose: /


        a_sol = [-1]*n
        self.putQueens(n, a_sol, f_col, f_downleft, f_downright, 0)
        return self.sols
