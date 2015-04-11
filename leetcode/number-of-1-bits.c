/*
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

  Cause we want to calculate the number of '1' bits in an 32-bit unsigned integer, which is a binary calculation.
  We should use MODULE-2 to test if the bit is 1 at the right end of the integer.
  And we use the Divided-By-2 (/=2) to move the 1 bit to the right of the integer. (除以二来将二进制表示的这个整数右移一位)
*/

int hammingWeight(uint32_t n) {
    int account = 0;
    while(n>0){
        account += n % 2;
        n /= 2;
    }
    return account;
}
