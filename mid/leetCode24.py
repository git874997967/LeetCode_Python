# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
             
        pre = dummyNode
         
        while pre.next and pre.next.next:
            cur = pre.next 
            post = pre.next.next 

            # pre cur post   swap
            cur.next = post.next 
            post.next = cur 
            pre.next = post 

            pre = pre.next.next 

        return dummyNode.next 
