#https://leetcode.com/problems/binary-tree-inorder-traversal/

# This piece of codes include 2 kind of solutions.
# One is recursive, which is easy to write and understand, but is trivial (简单的， 不重要的，无用的)
# The other is iterative, which is hard to think out, but may be asked in an interview.
# The iterative solution should use the stack data structure.
#
#In python, pop and append methods of a list can be used to implement a LIFO stack.
#pop: delete and return the last element of a list.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    ###SOLUTION 1: iteratively
    def iterativeSolution(self, root):
        out = []
        stack = []
        stack.append(root) #push the tree's root into the stack
        
        while len(stack) > 0:
            #go left to the end
            while stack[-1] :
                stack.append(stack[-1].left)
            
            #pop the last None node
            #THIS LINE IS VERY IMPORTANT!!!
            stack.pop()
            
            #cause we must have popped one node, 
            #but we may push nothing.
            #So we check if the stack is empty again.
            if len(stack)>0:
                #visit the middle node
                visit = stack.pop()
                out.append(visit.val)
                
                #push the right son of visit into the stack
                stack.append(visit.right)
                
        return out
   
    ###SOLUTION 2: recursively
    def __init__(self):
        self.out = []
    
    def recursiveSolution(self, root):

        if root:
            self.inorderTraversal(root.left)
            self.out.append(root.val)
            self.inorderTraversal(root.right)

        return self.out

    def inorderTraversal(self, root):
        return self.recursiveSolution(root)
