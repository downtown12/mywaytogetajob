<<<<<<< HEAD
=======
# My idea refers to this backtracing code:
# https://leetcode.com/discuss/31852/clean-c-code-using-backtrace-easy-to-understand
# The difference is: For each unfilled cell in the sudoku board, I search out all 
# the candate values could be filled into at one time. To do this, I define a function called findCandidates.
# The second point I want to talk about is how backtracing has been used in this problem:
# for each candidate could be filled in a cell, I firstly have a try and fill it. Then I filled the next one using recursion, and the next's next...Until either all cells has been filled with values(return True and the problem solved), 
# or no candidate is avaliable(finding out no candidate or having used up all candidates for one future cell), then we return False and do the becktrace.
# The backtrace is to set the source cell that cause this False-return back to the value of '.',
# Then the next candidate of this source cell can be tried.


>>>>>>> origin/master
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.fillSudoku(board,0,0)
    
    def fillSudoku(self, board, row, col):
<<<<<<< HEAD
        #Has already filled every hole
        if row == len(board):
            return True

        #print 'row:', row, ' col:',col
        if not board[row][col] == '.':
            #print 'row:', row, ' col:',col
            if col==len(board)-1:
=======
        #Has already filled every cell with values
        if row == len(board):
            return True

        if not board[row][col] == '.':
            if col>=len(board)-1:
>>>>>>> origin/master
                return self.fillSudoku(board, row+1, 0)
            else:
                return self.fillSudoku(board, row, col+1)

        cddts = self.findCandidates(board, row, col)
        #if find nothing
        if len(cddts) == 0:
            return False

        for i in cddts:
<<<<<<< HEAD
            #notice!
            #board[row] = board[row][:col] + [i] + board[row][col+1:]
            board[row][col] = i
            #print 'row:', row, ' col:',col
            if col == len(board)-1:
                if self.fillSudoku(board, row+1, 0): return True
                else: board[row][col] = '.'
            elif self.fillSudoku(board, row, col+1):
                return True
            else:
                #fillSudoku returns False
                #do backtracing
                #board[row] = board[row][:col] + ['.'] + board[row][col+1:]
                board[row][col] = '.'
=======
            #Here I use the former sentence to modify board
            #However, The latter one should be used for leetcode
            board[row] = board[row][:col] + i + board[row][col+1:]
            #board[row] = i
            if col == len(board)-1:
                if self.fillSudoku(board, row+1, 0):
                    return True
                else: board[row] = board[row][:col] + '.' + board[row][col+1:]
            elif self.fillSudoku(board, row, col+1):
                return True
            else:
                #if the above fillSudoku functions returns False,
                #do backtracing!
                #Here I use the former sentence to modify board
                #However, The latter one should be used for leetcode
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                #board[row] = i
>>>>>>> origin/master

        #has tried every possibility in cddts:
        return False
    
    
    def findCandidates(self, board, row, col):
        cddts = set(str(i) for i in range(1,10))
        horizontal = set([i for i in board[row] if not i == '.' ])
        vertical = set([board[i][col] for i in range(9) if not board[i][col] == '.'])
        grid = set(board[i][j] for i in range(row/3*3,row/3*3+3) for j in range(col/3*3,col/3*3+3) if not board[i][j] == '.')
<<<<<<< HEAD
=======
        #if row==0 and col==0:
>>>>>>> origin/master
        
        cddts -= (horizontal | vertical | grid)
        
        return list(cddts)
<<<<<<< HEAD
            
            
=======

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s = Solution()
s.solveSudoku(board)
for line in board:
	print line
>>>>>>> origin/master
