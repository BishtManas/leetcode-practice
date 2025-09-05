from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # swap while at least two nodes are available
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # perform the swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move prev ahead for next pair
            prev = first

        return dummy.next

# ---------- Helper Functions ----------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Convert Python list to linked list"""
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def list_from_head(head: Optional[ListNode]) -> List[int]:
    """Convert linked list back to Python list"""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

# ---------- Testing ----------
if __name__ == "__main__":
    s = Solution()
    examples = [
        [1, 2, 3, 4],
        [],
        [1],
        [1, 2, 3]
    ]
    for arr in examples:
        head = build_linked_list(arr)
        res = s.swapPairs(head)
        print()
        print(f"input: {arr} -> output: {list_from_head(res)}")
        print()
