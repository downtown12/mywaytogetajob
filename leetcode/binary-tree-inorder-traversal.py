#https://leetcode.com/problems/binary-tree-inorder-traversal/

#This is a iterative solution
#
#In python, pop and append methods of list can be used to implement a LIFO stack.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def iterativeSolution(self, root):
        out = []
        stack = []
        stack.append(root) #push the tree's root into the stack
       
        while len(stack) > 0:
            #go left to the end
            while stack[-1] :
                stack.append(stack[-1].left)
           
            #pop the last None node
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

    def inorderTraversal(self, root):
        return self.iterativeSolution(root)


if __name__ == '__main__':
    tree1 = TreeNode(1)
    node2 = TreeNode(2)
    tree1.left = node2
    sol = Solution()
    res = sol.inorderTraversal(tree1)
    print res
