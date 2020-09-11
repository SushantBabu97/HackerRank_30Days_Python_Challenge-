# BST Level-Order Traversals

"""
Task::: 
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right,
 top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. 
Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

Sample Input:::
6
3
5
4
7
2
1

Sample Output:::
3 2 5 1 4 7 

Explanation:::
We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. 
The resulting level-order traversal is 3->2->5->4->1->7, and we print these data values as a single line of space-separated 
integers.

"""

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = [ root ]
        for current in q:    
            if current:
                print(current.data, end=' ')

                q.append(current.left)
                q.append(current.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)


"""
-----------------------------------------------------------OR--------------------------------------------------------
        # queue = [root]
        # while len(queue) !=0:
        #     curr = queue[0]
        #     queue = queue[1:]
        #     print(str(curr.data) + " ", end="")

        #     if curr.left is not None:
        #         queue.append(curr.left)
        #     if curr.right is not None:
        #         queue.append(curr.right)
"""