class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


# --- Helper functions for testing ---
def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


# --- Example test ---
head = build_linked_list([4, 5, 1, 9])
node_to_delete = head.next   # node with value 5
Solution().deleteNode(node_to_delete)

print_linked_list(head)  # Output: [4, 1, 9]
