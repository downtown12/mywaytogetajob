class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        #calculate factorial from 1! to (n-1)!
        if n==1:
            return '1'
        
        factorial_n = [0]*(n-1)
        factorial_n[0] = 1
        for i in range(1,n-1):
            factorial_n[i] = (i+1)*factorial_n[i-1]
        #print "factorial_n: ", factorial_n
        
        tmp = k-1
        count = 0
        count_seq = []
        i = n-2 # the length of factorial_n is n-1
        while i>=0:
            count = tmp/factorial_n[i]
            
            count_seq.append(count)
            tmp -= factorial_n[i]*count
            i-=1

        #at last, append a 0. Standing for the last number to pick out.
        count_seq.append(0)
        #print count_seq
       
        numbers = [str(i) for i in range(1,n+1)]
        res = []
        for i in range(n):
            res.append(numbers[count_seq[i]])
            del numbers[count_seq[i]]
        
        #res.append[numbers[0]]
        
        return ''.join(res)


s = Solution()
print s.getPermutation(2,1)
