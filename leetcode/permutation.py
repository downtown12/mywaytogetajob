'''
Using Two list. One is named choosed who records the numbers having been choosed into a permutation, the other is named candidates in which will be choosed one to add into choosed list for the next time.
When candidates shrinks to an empty list. A permutation of all the given numbers is generated in the choosed list.
So I need to do is traversing all the possibilities of the chosen one for each index.
For example, as [1,2,3] for input.
index 0 has three possibilities([choosed],[candidates]): [1],[2,3]; [2],[1,3] and [3],[1,2]

Then [1],[2,3] has two possibilities for index 1: [1,2],[3] and [1,3],[2],
     [2],[1,3] has two possibilities for index 1: [2,1],[3] and [2,3],[1],
     [3],[1,2] has two possibilities for index 1: [3,1],[2] and [3,2],[1].
     
Then for the last index: each possibilities above has only one candidate. Choose the only one.
Then all the permutations are generated, they are [123],[132],[213],[231],[312],[321]
'''

class Solution:
    def __init__(self):
        self.allpermutations = []
        
    def findPermutations(self, choosed, candidates):
        if len(candidates)==0:
            self.allpermutations.append(choosed[:])
            return
        for i in range(len(candidates)):
            choosed.append(candidates[i])
            del candidates[i]
            self.findPermutations(choosed, candidates)
            #backtracing
            candidates.insert(i, choosed.pop())

    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        #allpermutations = []
        choosed = []
        candidates = nums[:]
        self.findPermutations(choosed, candidates)
        return self.allpermutations
        
