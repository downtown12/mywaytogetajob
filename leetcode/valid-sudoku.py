'''
The uses of Hashmap in this problem are:
    Maps the status of whether a number has occured or not to boolean list.
    I create three lists to record the true-or-false status of a number has occured in a line, a row, or a 3*3-grid.
    Each list of the three has 9 element. A number in the sudoku table maps to the index that equals to number's value -1 of the list.
    So it is an index-to-value map.
'''
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        num_row = [[False] * 9 for i in range(9)]
        num_col = [[False] * 9 for i in range(9)]
        num_grid = [[False] * 9 for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                cur = int(board[i][j])
                #already occurs
                if num_row[i][cur-1] or num_col[j][cur-1] or num_grid[(i/3)*3+j/3][cur-1]:
                    return False
                
                num_row[i][cur-1] = True
                num_col[j][cur-1] = True
                num_grid[(i/3)*3+j/3][cur-1] = True
                
        
        return True
