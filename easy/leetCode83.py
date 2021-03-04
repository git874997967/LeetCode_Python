# 83. Remove Duplicates from Sorted List
# solution  not that hard  just use a cur to track current node and next node
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    if head == None or head.next == None:
        return head
    cur = head
    while (cur != None and cur.next != None):
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next 
    
    return head

    if head == None or head.next == None:
        return head
    cur = head
    while cur != None and cur.next != None:
        while cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    
    return head
        
