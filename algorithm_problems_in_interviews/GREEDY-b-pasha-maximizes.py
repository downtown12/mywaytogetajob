'''
Asked during MEITUAN test&devlopment intern interview

THE PROBLEM'S DESCRIPTION:
=========================
  Pasha has a positive integer a without leading zeroes. Today he decided that the number is too small and he should make it larger. Unfortunately, the only operation Pasha can do is to swap two adjacent decimal digits of the integer.

Help Pasha count the maximum number he can get if he has the time to make at most k swaps.

Input
The single line contains two integers a and k (1 ≤ a ≤ 1018; 0 ≤ k ≤ 100).

Output
Print the maximum number that Pasha can get if he makes at most k swaps.

Sample test(s)
input
1990 1
output
9190

THE FULL DESCRPTION AND CODE SUBMISSION:
=======================================
http://codeforces.com/contest/435/problem/b

THE IDEA IS:
============
Use the greedy thought.
That is, make the higher digit the max one within k steps is more important. 
So I make the highest digit as big as possible in k step t. 
After that, if I still spare (k - used) steps, like what I've just done, 
I use these steps to make the second highest as big as possible
repeat this procedure until I run out of all of my k steps, or every digit of the number is the biggest one.(from higher to lower digit, the value is from bigger to smaller) 

NOTE:
====
1. To compare digits, I convert the input number to a list. Each element in this list is a digit of the number.
2. For each digit, I set a pivot to find the biggest value this digit can be within the steps I still have.
'''
def findMax(a, k):
	for i in range(0, len(a)-1):
		#init
		pivot = i+1
		index_max = i
		digit_max = a[i]

		#find how big the current digit can be in k steps.
		while pivot-i <= k and pivot <len(a):
			if a[pivot] > digit_max:
					digit_max = a[pivot]
					index_max = pivot
			pivot += 1

		#do swaps to make this digit as big as possible
		for  j in range(index_max,i,-1):
			a[j],a[j-1] = a[j-1],a[j]
			k -= 1
		
		if k<=0 :
				break
	
	num = 0
	for i in a:
		num *=10
		num += i
	return num

if __name__ == '__main__':
	line = raw_input()
	(astr,kstr) = tuple(line.split(' '))
	alist = [int(i) for i in astr]
	print findMax(alist,int(kstr))
