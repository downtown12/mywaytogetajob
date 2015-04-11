'''
https://leetcode.com/problems/maximum-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
		If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

#This is an O(n) solution.
#思路是：
#遍历一遍数组，便利到某个元素A[j]时：
#通过两个
#用max_so_far记录遍历到此处时已经找到的子数组的最大和
#potential_max记录便利到此处的前一个位置上，仍有潜力成为最大子数组的子数组和。
#potential_max是这样变化的，遍历到元素A[j]时,若sum(A[i...j-1])>=0，就仍有增长成为目前的最大子数组的可能。如果potential_max<0，因为负数只可能让相加的结果更小，所以以A[j-1]结尾的子数组不可能是最大子数组了,就将potential_max重置为0.也可理解为现在要从当前位置（A[j]）重新寻找potential_max了。
#现在，无论potential_max重置与否，都将potential_max += A[j]

#接下来，若potential_max>max_so_far了，就更新max_so_far的值

#注意：由于potential_max和max_so_far的初始值为0。需要考虑的一种特殊情况是全为负数的数组，例如:[-1]。 这个例子，leetcode测试用例应该返回-1作为最大子数组的和。
#处理这种特殊情况地方法就是：设置一个记录是否为全负数数组的标志位:all_negtive. 初始值为True，若数组出现了非负数，就将它设为False。
#遍历完数组后，若仍为False，就再遍历一遍数组，取其中最大的负数作为返回值。

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        potential_max = 0
        max_so_far = 0
        
        all_negtive = True
        
        for x in A:
            #especially consider of that the all elements in A are negtive
            if x >= 0:
                all_negtive = False
            
            if potential_max < 0:
                #reset to 0
                potential_max = 0

            potential_max += x
            
            if potential_max > max_so_far:
                max_so_far = potential_max
        
        if all_negtive == True:
            max_neg = max([x for x in A if x<0])
            return max_neg
            
        return max_so_far
