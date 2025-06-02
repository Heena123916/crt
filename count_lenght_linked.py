class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                count=1
                slow=slow.next
                while(slow!=fast):
                    slow=slow.next
                    count+=1
                return count
        return 0            
