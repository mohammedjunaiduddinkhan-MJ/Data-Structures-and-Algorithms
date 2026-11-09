# Problem: Reverse a Doubly Linked List
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

def reverse(head):
    if head is None:
        return head

    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next, current.prev = current.prev, current.next
        prev = current
        current = next_node

    return prev

#Time Complexity = O(N) – Traversing the linked list once.
#Space complexity = O(1) – Using only two pointer variables(prev,current).