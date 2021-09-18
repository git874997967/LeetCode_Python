# 206. Reverse Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(self, head):
        if not head or head.next is None:
            return head 
        prev, cur ,next = None, head,head 
        while cur:
          cur.next, pre, cur = pre, cur,cur.next 
        return prev 


    def reverseList(self, head):
        if not head or head.next is None:
            return head 
        prev, cur   = None, head  
        while cur:
           temp = cur.next
           cur.next = prev 
           prev = cur
           cur = temp
        return prev 



