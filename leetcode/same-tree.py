'''
https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


The basic idea is do a Root-Left-Right traverse for the two trees.
Here I use a RECURSIVE way.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        #extreme condition
        if p==None and q==None:
            return True
        
        #both p and q are not None, which is the most common condition.
        elif (not p== None) and (not q==None):
            if not p.val == q.val:
                return False
            elif self.isSameTree(p.left, q.left) == False:
                return False
            #p.left and q.left are the same trees
            elif self.isSameTree(p.right, q.right) == False:
                return False
            else: return True
        
        #One of p or q is None while the other one is not. 
        else: return False
