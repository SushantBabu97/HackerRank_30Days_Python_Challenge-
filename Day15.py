#Linked List

"""
A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer data value that must be added 
to the end of the list as a new Node object.

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head=Node(data)
        else:
            curr=head
            while curr.next:
                curr=curr.next
            curr.next=Node(data)
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  


"""
Sample Input::
The following input is handled for you by the locked code in the editor: 
The first line contains T, the number of test cases. 
The T subsequent lines of test cases each contain an integer to be inserted at the list’s tail.

4
2
3
4
1

Sample Output::
The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:
2 3 4 1

Explanation::
T = 4, so the locked code in the editor will be inserting 4 nodes. 

The list is initially empty, so head is null; accounting for this, 
our code returns a new node containing the data value 2 as the head of our list.  
We then create and insert nodes 3, 4, and 1 at the tail of our list. 
The resulting list returned by the last call to insert is [2, 3, 4, 1], so the printed output is 2 3 4 1.

"""