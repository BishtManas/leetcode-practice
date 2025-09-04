from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

def pretty(head: Optional[ListNode]) -> str:
    return " -> ".join(map(str, to_list(head))) if head else "[]"

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy

    # move fast n steps
    for _ in range(n):
        fast = fast.next

    # move both until fast hits the last node
    while fast.next:
        fast = fast.next
        slow = slow.next

    # delete the node after slow
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    # Example 1
    head = build_linked_list([1,2,3,4,5])
    n = 2
    print("Input :", pretty(head), " n =", n)
    result = remove_nth_from_end(head, n)
    print("Output:", pretty(result))  # [1,2,3,5]

    # Example 2
    head = build_linked_list([1])
    n = 1
    print("\nInput :", pretty(head), " n =", n)
    result = remove_nth_from_end(head, n)
    print("Output:", pretty(result))  # []

    # Example 3
    head = build_linked_list([1,2])
    n = 1
    print("\nInput :", pretty(head), " n =", n)
    result = remove_nth_from_end(head, n)
    print("Output:", pretty(result))  # [1]
