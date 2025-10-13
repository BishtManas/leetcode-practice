# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head

        # Compute length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        # Split helper function
        def split(start, n):
            """
            Split list starting at `start` into two parts:
            - first part contains up to n nodes
            - returns the head of the second part
            """
            if not start:
                return None
            cur = start
            for _ in range(n - 1):
                if cur.next:
                    cur = cur.next
                else:
                    break
            second = cur.next
            cur.next = None
            return second

        # Merge helper function
        def merge(l1, l2):
            """
            Merge two sorted lists l1 and l2.
            Return (merged_head, merged_tail).
            """
            tail = ListNode(0)
            ptr = tail
            a, b = l1, l2
            while a and b:
                if a.val <= b.val:
                    ptr.next = a
                    a = a.next
                else:
                    ptr.next = b
                    b = b.next
                ptr = ptr.next

            ptr.next = a if a else b
            while ptr.next:
                ptr = ptr.next
            return (tail.next, ptr)

        # Bottom-up merge sort
        while size < length:
            prev = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = split(left, size)
                cur = split(right, size)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1

        return dummy.next


# ---------------------- #
# Helper functions for testing
# ---------------------- #

def build_linked_list(values):
    """Convert Python list to linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    """Convert linked list back to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------------------- #
# Test the sortList function
# ---------------------- #

if __name__ == "__main__":
    sol = Solution()

    # Example test cases
    test_cases = [
        [4, 2, 1, 3],
        [-1, 5, 3, 4, 0],
        [],
        [1],
        [2, 1]
    ]

    for arr in test_cases:
        head = build_linked_list(arr)
        sorted_head = sol.sortList(head)
        print(f"Input: {arr} → Output: {linked_list_to_list(sorted_head)}")
