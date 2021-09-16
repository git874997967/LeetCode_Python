#445 Add two numbers II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack3 ,stack1,stack2 = [],[],[]
        
        flag = 0
        dummy = ListNode(0)
        current = dummy
        while l1:
            stack1.append(l1.val)
            l1 = l1.next 
        while l2:
            stack2.append(l2.val)
        while stack1 and stack2:
            flag,val = divmod(stack1.pop() + stack2.pop() + flag, 10)  
            stack3.append(val)
             
            
        while stack1:
            flag,val = divmod(stack1.pop() + flag, 10)  
            stack3.append(val)

        
        while stack2:
            flag,val = divmod(stack2.pop() + flag, 10)  
            stack3.append(val)
        
        if flag:
            stack3.append(flag)

        while stack3:
            current.next = ListNode(stack3.pop())
            current = current.next 

        return dummy.next 
            