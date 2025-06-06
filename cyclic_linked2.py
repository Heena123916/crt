class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next   # <-- Fix: move fast, not reassign head
                return slow         # <-- Fix: return after loop ends
        return None
