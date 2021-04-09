# 206. Reverse Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(self, head):
        if not head or head.next is None:
            return head 
        prev, cur = None, head 
        while cur:
            cur.next,prev,cur = prev,cur,cur.next 
        return prev 



