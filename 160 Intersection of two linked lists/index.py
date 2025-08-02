class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

# 🚀 Test Code Example
# Create common part: 8 -> 4 -> 5
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# Create List A: 4 -> 1 -> [8 -> 4 -> 5]
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

# Create List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

# Call the function
intersection = getIntersectionNode(headA, headB)

# 🧾 Output the result
if intersection:
    print("Intersected at:", intersection.val)
else:
    print("No intersection")
