# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(l1,l2) :
    # dummy node for head is a must  
    # the real list starts at dumm.next  which we return that 
    resultHead = listNode(-1)
    result = resultHead
    while l1 and l2:
        if l1.val <= l2:
            result.next = l1
            l1 = l1.next
        else:
            result.next = l2
            l2 = l2.next
        result = result.next
    result. next = l1 if l1 is not None else l2 
    return resultHead.next

# solution 2
def mergeTwoLists2(l1,l2):
    if l1 is None :
        return l2
    if l2 is None: 
        return l1
    elif l1.val <= l2.val:
        self.l1 =  mergeTwoLists2(l1.next,l2)
        return l1
    else :
        self.l2 = mergeTwoLists(l1,l2.next)
        return l2
    