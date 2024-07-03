/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> vis = new HashSet<>();
        ListNode curr = head;
        
        while (curr != null) {
            if (vis.contains(curr)) {
                return true;
            }
            vis.add(curr);
            curr = curr.next;
        }
        
        return false;
    }
}
