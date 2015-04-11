'''
https://leetcode.com/problems/single-number-ii/

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
		Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



Copied from: https://leetcode.com/discuss/24329/12ms-iteration-variables-reset-with-algorithm-description

The basic idea is to implement a modulo-3 counter (to count how many times "1" occurs) for each bit position.
Such modulo-3 counter needs two bits (B1,B0) to represent. 
(B1,B0): 
(0, 0) : '1' occurs zero times after last resetting,
(0, 1) : '1' occurs one times after last resetting,
(1, 0) : '1' occurs two times after last resetting,
(1, 1) : '1' occurs three times after last resetting, then we need to reset the counter to (0,0)
So to implement such modulo-3 counters, we need three variables (b0, b1, reset)
The n-th bit of b0 is the B0 bit of the modulo-3 counter for the n-th bit (n=0..31 assuming int is 32 bit)
The n-th bit of b1 is the B1 bit of the modulo-3 counter for the n-th bit (n=0..31 assuming int is 32 bit)
The n-th bit of reset is the reset flag of the modulo-3 counter for the n-th bit (n=0..31 assuming int is 32 bit), 

- b0: can be easily implemented with XOR bit operation,  as b0 = b0^ A[i]
- b1: B1 will only be set to 1, when B0 (of the n-th bit counter) =1 and the n-th bit of A[i] = 1, and stay '1' until it is reseted. So b1 |=  b0 & A[i]; 
- The reset flag is set when (B1, B0) = (1,1). So, reset = b0 & b1;
- The reset operation can be done by b0 = b0 ^ reset and b1 = b1 ^ reset;

After updating the b0, b1, reset with all A[], the b0 will be the final result since if the n-th bit of the to-be-found element is 1, then the times of '1' occurs on the n-th bit is 3*x+1, which is 1 after the modulo 3 opertation.   
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        #bit0,bit1 and reset-flag make an modulo-3 counter
        bit0 = 0
        bit1 = 0
        reset = 0
        
        for num in A:
            bit1 |= bit0 & num
            bit0 = bit0 ^ num
            reset = bit0 & bit1 #reset flag is true when both bit0 and bit1 are 1, that is (1,1)
            #reset is true only when both bit0 and bit1 are 1, so we can use xor operation to reset bit0 and bit1
            #without this precondition, bit0 (or bit1) is 0 may become 1 after resetting.
            bit0 = bit0 ^ reset
            bit1 = bit1 ^ reset
        
        #now b1 is 0 (I think) because every other element occurs 3 times except the single one.
        #so the second bit of this modulo-3 counter (that is bit1) is resetted to 0.
        #now b0 is the 
        return bit0
