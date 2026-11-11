# Problem: Linked List Cycle II
# Problem Number: 142
# Platform: Leetcode

def detectCycle(head): 
    slow ,fast = head,head
    while((fast is not None) and (fast.next is not None)):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            break
    else:
        return None
    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    return fast

# Time Complexity : O(N)
# Space Complexity : O(1)