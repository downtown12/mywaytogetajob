'''
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
		Given array A = [2,3,1,1,4]

		The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

#This is a Greedy algorithm to solve this problem and it has linear time cost.
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)

        if n ==0 or n == 1: 
                return 0

        #步数
        step = 0
        
        #mark the furthest index the former step can reach.
        #记录上一次迈步时可以到达的最远坐标
        last_in_former_step = 0
        #last: a dynamic updating value. 
        #It refers to the furthest distance can be reached from an index in one step
        #记录当前坐标用一步所能到达的范围中，再用一步能到达的最远距离。它是动态更新的。
        last = 0

        for i in range(n):
                if i + A[i] >= n-1:
                        return step+1
                #if we can reach further by one step
                if i+A[i] > last:
                        last = i + A[i]

                #if this one step can't reach further, step one step (update variable step)
                if i >= last_in_former_step:
                        step += 1
                        last_in_former_step = last

