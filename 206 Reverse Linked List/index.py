class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverseListRecursive(self, head):
 
        if head is None or head.next is None:
            return head

        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)

solution = Solution()


reversed_head = solution.reverseList(head)
print("Iterative Reverse:")
print_linked_list(reversed_head)


head = create_linked_list(arr)


reversed_head_recursive = solution.reverseListRecursive(head)
print("Recursive Reverse:")
print_linked_list(reversed_head_recursive)