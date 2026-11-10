# Problem: Remvoe duplicates from a Sorted Doubly linked list
# Platform: GeeksforGeeks

def removeDuplicates(headRef):
        current = headRef 
        while(current is not None):
            if((current.prev is not None) and (current.data == current.prev.data)):
                duplicate = current.prev
                if(duplicate == headRef):
                    headRef = current
                    current.prev = None
                else:
                    duplicate.prev.next = current
                    current.prev = duplicate.prev
                duplicate.next = None
                duplicate.prev = None
            else:
                current = current.next
        return headRef

# Time complexity: O(n) — one traversal.
# Auxiliary space: O(1) — no additional data structures.