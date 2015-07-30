class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        D = dict()
        for i in nums:
            if i in D:
                return True
            else:
                D[i] = True
        
        return False
