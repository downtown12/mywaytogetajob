'''
Refer to: https://leetcode.com/discuss/38492/shortest-c-solution-in-0ms
Faster than the way refered above (not using class member but a local variable in putQueens) which costs 72ms
My code below using a class member called sumofsols to record total number of solutions.
And my code costs 68ms after delete these comment lines.
'''

class Solution:
    def __init__(self):
        self.sumofsols = 0
        
    def putQueens(self, n, f_col, f_downleft, f_downright, row):
        if row==n:
            self.sumofsols+=1
            return
        
        for col in range(n):
            if f_col[col] and f_downleft[row+col] and f_downright[n-row+col-1]:
                #valid to put a queen
                f_col[col] = f_downleft[row+col] = f_downright[n-row+col-1] = False
                self.putQueens(n,f_col,f_downleft,f_downright,row+1)
                f_col[col] = f_downleft[row+col] = f_downright[n-row+col-1] = True
            
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        f_col = [True]*n
        f_downleft = [True]*(2*n-1)
        f_downright = [True]*(2*n-1)
        self.putQueens(n, f_col, f_downleft, f_downright, 0)
        return self.sumofsols
        
