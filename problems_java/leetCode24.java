package problems_java;
 public class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
public class leetCode24 {
    public stattic ListNode(ListNode head){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while(prev.next != null && prev.next.next != null){
             ListNode cur = prev.next;
             ListNode post = prev.next.next;

             // start the swap
             cur.next = post.next;
             post.next = cur;
             prev = post;

             prev = prev.next.next;
        }
        return dummy.next;
    }
    public static void main(String[] args){
    }
}
