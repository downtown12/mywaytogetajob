'''
My solution has a 2O(n) time complexity

Before solving this problem, one important thing to keep in mind is:
    An array is a random storage structure, but not a linked list.
    It means you can get a random element in array by giving its index immediately.

The key to copying a linked list with random pointer is how to quickly assign each cloning node's 'random' attribute.
because if the new cloning linked list is only a linked list, we can't find which node its random pointer points to quikly (in O(1) time complexity).

But if I have these two factors below, I can find where its random pointer points quickly:
1. Make a hashmap which map to the original list's node to its position(start from 0) in this list.
2. Make the new cloning list not just a linked list, but also an array.

The original linked list and the cloning one share the same element's index,
so I can map the node random pointer points to its index from the hashmap created in the factor 1.
then I can get a cloning node's random attribute by this index I just get quickly, because the cloning list is also an array.

a node: [label | random | next ]

Orignal Linked list:

   |-----------------------------------|
   V                                   |
[node1| |-]----> [node2|^|-]---->[node3| |^]
       |                            ^
       |____________________________|

hashmap: 
node:       index   random's index  cloning nodes   
node1       0       2               node1'
node2       1       None            node2'
node3       2       0               node3'

cloning array:
    0       1       2
[node1', node2', node3']
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        #extreme condition: empty list
        if head ==None:
            return head
        
        cur = head
        node2index = dict()
        #copy2orig = dict()
        i=0 #index counter
        l_cloners = []

        #Traverse for the first time
        while cur:
            node2index[cur] = i
            i+=1
            l_cloners.append(RandomListNode(cur.label))
            #copy2orig[ l_cloners[-1] ] = cur
            cur = cur.next

        #Traverse for the second time
        #cause i want to link the next pointer for each node this time,
        #I do not consider the last element at the beginning.
        cur = head
        for i in range(len(l_cloners)-1):
            #assign next
            l_cloners[i].next = l_cloners[i+1]

            if cur.random:
                random_index = node2index[cur.random]
                #assign random
                l_cloners[i].random = l_cloners[random_index]

            cur = cur.next

        #tackle with the last element
        if cur.random:
            random_index = node2index[cur.random]
            #assign random
            l_cloners[-1].random = l_cloners[random_index]

        return l_cloners[0]

if __name__ == '__main__':
	llist = [RandomListNode(i) for i in range(1,5)];
	for node,nnode in zip(llist[:-1], llist[1:]):	
		node.next = nnode
	
	llist[0].random = llist[2]
	llist[1].random = llist[2]
	llist[2].random = None
	llist[3].random = llist[0]

	s = Solution()
	s.copyRandomList(llist[0])
