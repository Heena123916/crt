class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        # Move slow pointer by 1 step
            fast = fast.next.next   # Move fast pointer by 2 steps
            
            if slow == fast:        # If slow and fast meet, there's a cycle
                return True
        
        return False  # If fast reaches the end (None), there's no cycle

        
