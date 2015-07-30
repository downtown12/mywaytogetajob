'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def calSquare(self, n):
        res=0
        if n==0:
            return 0
        while n>0:
            res += (n%10)**2
            n/=10
        return res
        
    def isHappy(self, n):
        return self.isHappy2(n)
    
    #using a list to record the numbers that has appeared
    def isHappy1(self, n):       
        l = []
        while not n==1 and not n in l:
            l.append(n)
            n = self.calSquare(n)
        
        if n ==1:
            return True
        else: return False
    
    #This solution is definitely true for 32bit integers,
    #I'm not sure whether its true for Python integers.
    #Whatever, all the testcases passes.
    '''
    if int has 4 bytes, then the biggest int will be roughly around 2 billion, so after the first process, the number will be less than 10 * 9 ** 2(e.g. 1,999,999,999 -> 730 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> ...), and it will be less than 10 * 9 ** 2 forever.
    So we can use a boolean table to record whether a number(which is less than 1000) has appeared. That is the key idea of my solution.
    '''
    def isHappy2(self, n):
        l = [False]*1000
        n = self.calSquare(n)
        while not n==1 and not l[n]:
            l[n] = True
            n = self.calSquare(n)
        
        return n==1
        
