from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next

# Helper: Convert list to linked list
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper: Convert linked list to list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# === TESTING ===
if __name__ == "__main__":
    sol = Solution()
    
    input_list = [1, 4, 3, 2, 5, 2]
    x = 3
    head = list_to_linked_list(input_list)
    
    result_head = sol.partition(head, x)
    output_list = linked_list_to_list(result_head)
    
    print("Input list:", input_list)
    print("Partitioned list with x =", x, "->", output_list)
