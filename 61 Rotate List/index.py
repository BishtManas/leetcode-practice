class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Get length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make it circular
        tail.next = head

        # Step 3: Find new tail
        k %= length
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 4: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head

# -------- Helper functions to test in VS Code --------
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# -------- Example usage --------
if __name__ == "__main__":
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    k = 2
    solution = Solution()
    rotated_head = solution.rotateRight(head, k)
    print(linkedlist_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]
