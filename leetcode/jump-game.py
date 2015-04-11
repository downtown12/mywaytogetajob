'''
https://leetcode.com/problems/jump-game/
'''


class Solution:                               
    # @param A, a list of integers            
    # @return a boolean                       
    def canJump(self, A):
            length   = len(A)
            #if A is a [] list
            if length == 0:
                    return False
            
            # init maxDis = 0, 
            # because BEFORE ARRIVING at the index 0, we can't jump any distance, that is 0.
            maxDis = 0
            for i in range(length):
                    if maxDis < i:
                            return False

                    if maxDis< A[i] + i:
                            maxDis = A[i]+i
                           
                    if maxDis>= len(A)-1:
                            return True
