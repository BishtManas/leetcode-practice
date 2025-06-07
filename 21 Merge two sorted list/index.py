# Define your ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to merge two lists
def mergeTwoLists(list1, list2):
    # Dummy node to start the result list
    dummy = ListNode(0)
    current = dummy
    
    # While both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If any list is not empty, connect it to the result
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    # Return the merged list (skip dummy node)
    return dummy.next

# Function to print the linked list (just for your understanding)
def printList(node):
    while node:
        print(node.val, end=",")
        node = node.next

# Function to create a linked list from a list (so you can update lists easily!)
def createLinkedList(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Example usage:

# You can update your lists here:
list1_values = [1, 3, 5]
list2_values = [2, 4, 6]

list1 = createLinkedList(list1_values)
list2 = createLinkedList(list2_values)

# Merge them
merged_list = mergeTwoLists(list1, list2)

# Print result
printList(merged_list)
