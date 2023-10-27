from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head   # Initialize two variables, prev and curr, to None and the input head

        while curr:   # Start a loop that continues as long as curr is not None (as long as there are more nodes to process)
            nxt = curr.next   # Create a new variable called nxt to store the next node in the original list
            curr.next = prev  # Update the next pointer of the current node (curr) to point to the previous node (prev)
            prev = curr   # Move prev and curr one step forward in the list
            curr = nxt
        return prev
