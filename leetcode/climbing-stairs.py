#Climbing Stairs
#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#

#My idea of DP:
#Say n is the number of stairs to be climbed.
#Say f(n) is the number of ways for me to climb n stairs

# Cuz I can climb one stair or two stairs once, 
# So the transferring formula is:
#     f(n) = f(n-1) + f(n-2)
# 
# The end situation is:
#         if n==1, f(n) = 1 #climb one stair once.
#         if n==2, f(n) = 2 #climb two stairs once or climb one stairs twice.

class Solution(object):
    def climbStairs(self, n):
       """
       :type n: int
       :rtype: int
       """
       if n==1 or n==0:
               # if n==1, climb one stair once.
               # if n==0, staightly reach the top, climb no stairs can also be seen as a way.
               return 1
       elif n==2:
               #climb two stairs once or climb one stairs twice.
               return 2
       else:
               f = [1,2] + [0] * (n-2)
               #Below is the transferring formula: 
               for i in range(2,n):
                       f[i] = f[i-1] + f[i-2]

               return f[n-1]

import sys
n = int(sys.argv[1])
s = Solution()
print s.climbStairs(n)

