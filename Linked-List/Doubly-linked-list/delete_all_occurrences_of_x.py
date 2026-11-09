# Problem: Delete All Occurrences of a Given Key in a Doubly Linked List
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

def deleteAllOccurOfX(head, x):
    if(head is None):
        return None
    current = head
    while(current is not None):
        next_node = current.next
        if(current.data == x):
            if(current.prev is None):
                head = head.next
                current.next.prev = None
                
            elif(current.next is None):
                current.prev.next = None
            else:
                current.prev.next = next_node
                current.next.prev = current.prev
            current.next = None
            current.prev = None
        current = next_node
        
    return head