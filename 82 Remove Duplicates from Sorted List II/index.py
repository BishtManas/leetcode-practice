# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node to handle edge cases, like removing the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # This will keep track of the node before the duplicate sequence
        
        while head:
            # Check if the current node is a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes that have the same value as the current node
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip the duplicate nodes
                prev.next = head.next
            else:
                # No duplicates, move prev to the next node
                prev = prev.next
            head = head.next
        
        return dummy.next

# Helper function to convert list to ListNode
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
head = to_linked_list([1, 2, 3, 3, 4, 4, 5])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head)
