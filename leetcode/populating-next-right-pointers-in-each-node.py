# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
This is an recursive and depth-first search solution.
The code is simple and clear.
The main idea is that,
Firstly we connect a node's(if not None) left son to it's right son
then connect the node's right son to it's next's (if it has) left.

You may ask if this condition may happen?
         1
       /  \
      2 -X-3     //can it happen that the next-link from 2 to 3 is not connected,
     / \  / \
    4->5??6  7  //then we want to connect from 5 to 6 it won't work。。

The answer is,it never happens. And every possible next-link in the tree will be connected.
because at the first step we already link a next-linknode's left to its right, it can make sure that every next-link geometrically below this will be connected.
         1
       /  \
      2 -> 3     //firstly the next-link from 2 to 3 is connected,then it makes sure that
     / \  / \
    4->5->6  7   //every link geometrically below the 2->3 link will be connected (such as 5->6 in this level)  
   / \/\  /\ /\
        ...   
'''

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #special condition
        if root == None:
            return
        
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
