# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #t[i] is the list of BSTs who store numbers from 1 to i.
        #t[0] is an empty tree.
        t = [[None]] + [[] for i in range(n)]
        print t
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                #use j as the root of a BST who store numbers from 1 to i
                for ls in t[j-1]: #for each left subtree
                    for rs in t[i-j]: #for each right subtree
                        newnode = TreeNode(j)
                        newnode.left = ls
                        newnode.right = self.recursiveEachNodeAdd(rs, j)
                        t[i].append(newnode)
        
        return t[n]
                        
    def recursiveEachNodeAdd(self, rs, j):
        if not rs:
            return None
        
        newnode = TreeNode(rs.val + j)
        newnode.left = self.recursiveEachNodeAdd(rs.left, j)
        newnode.right = self.recursiveEachNodeAdd(rs.right, j)
        return newnode

#node = TreeNode(1)
s = Solution()
s.generateTrees(1)

