/*
  https://leetcode.com/problems/single-number/

Description:
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

The trick:
  The key to this problem is the bit exclusive or(xor) operation.
  because the xor operation result of two same number is 0.
  and luckily the the feature of the given array is that "every element appears twice except for one".
  so the xor result of all the numbers in the array is the single one.
  
*/

int singleNumber(int A[], int n) {
    int i = 0;
    int result = 0;
    for(i=0; i<n; i++){
        result ^= A[i];
    }
    return result;
}
