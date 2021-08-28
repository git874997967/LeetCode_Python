# 234. Palindrome Linked List
def isPalindrome(head):
       prev = None 
       slow = head
       fast = head 
       while  fast is not None and fast.next is not None :
           fast = fast.next.next 
           next = slow.next 
           slow.next = prev  
           prev = slow 
           slow = next
       if fast.next is not None:
           slow = slow.next 

       while slow is not None:
           if slow.val != prev.val:
               return False 
           prev,slow = prev.next ,slow.next 
       return True
     