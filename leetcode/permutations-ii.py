class Solution:
    def __init__(self):
        self.res = []
    
    def doPermutation(self, choosed, candidates):
        if len(candidates)==0:
            self.res.append(choosed[:])
            return
        
        num_occured = None
        for i in range(len(candidates)):
            if candidates[i]!=num_occured:
                tmp = num_occured = candidates[i]
                choosed.append(tmp)
                del candidates[i]
                self.doPermutation(choosed, candidates)
                #do backtracking
                candidates.insert(i,choosed.pop())
                
                
                
        
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        choosed = []
        candidates = nums[:]
        candidates.sort()
        self.doPermutation(choosed,candidates)
        return self.res

s = Solution()
print s.permuteUnique([1,1,2])
