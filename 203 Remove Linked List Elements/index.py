class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

# 🔽 Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 🔽 Helper function to convert linked list back to list for printing
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# ✅ Example use
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
val = 6

sol = Solution()
new_head = sol.removeElements(head, val)
print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 4, 5]
