# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head

        # Function to split the list into two halves
        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None  # Split the list into two halves
            return head, mid  # Return the two halves

        # Function to merge two sorted lists
        def merge(left, right):
            dummy = ListNode(0)
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right  # Append the remaining nodes
            return dummy.next

        # Split the list into two halves
        left_half, right_half = split(head)

        # Sort each half recursively
        sorted_left = self.sortList(left_half)
        sorted_right = self.sortList(right_half)

        # Merge the sorted halves
        return merge(sorted_left, sorted_right)

