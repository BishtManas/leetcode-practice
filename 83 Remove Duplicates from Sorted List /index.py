class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# 🔧 Quick setup and test
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(3)

# Run the function
head = deleteDuplicates(a)

# Print the result
while head:
    print(head.val, end=" -> ")
    head = head.next
print("None")
