class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.fillSudoku(board,0,0)
    
    def fillSudoku(self, board, row, col):
        #Has already filled every hole
        if row == len(board):
            return True

        #print 'row:', row, ' col:',col
        if not board[row][col] == '.':
            #print 'row:', row, ' col:',col
            if col==len(board)-1:
                return self.fillSudoku(board, row+1, 0)
            else:
                return self.fillSudoku(board, row, col+1)

        cddts = self.findCandidates(board, row, col)
        #if find nothing
        if len(cddts) == 0:
            return False

        for i in cddts:
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

        #has tried every possibility in cddts:
        return False
    
    
    def findCandidates(self, board, row, col):
        cddts = set(str(i) for i in range(1,10))
        horizontal = set([i for i in board[row] if not i == '.' ])
        vertical = set([board[i][col] for i in range(9) if not board[i][col] == '.'])
        grid = set(board[i][j] for i in range(row/3*3,row/3*3+3) for j in range(col/3*3,col/3*3+3) if not board[i][j] == '.')
        
        cddts -= (horizontal | vertical | grid)
        
        return list(cddts)
            
            
