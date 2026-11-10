# Problem: 237. Delete Node in a Linked List
# Platform: Leetcode


def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next

#Time Complexity = O(1) – No traversing.
#Space complexity = O(1) – 