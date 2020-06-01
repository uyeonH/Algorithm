# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
            
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        copy=head
        
        while (head):
            count+=1
            head=head.next
            
        count=count/2
        print(count)

        for i in range(int(count)):
            copy=copy.next
        
        return copy
    
