# Delete Node in a Linked List

## Problem
Given a node in a singly linked list, delete that node without having access to the head of the linked list.

**Constraint:** The given node is guaranteed not to be the last node, and all node values are unique.

## Approach 1: Brute Force (O(N))

Initially, I solved this problem by traversing the linked list starting from the given node.

- Used two pointers, `prev` and `current`.
- Copied the value of each subsequent node into the previous node.
- Continued until reaching the last node.
- Removed the last node by setting `prev.next = None`.

**Complexity Analysis:**
- Time Complexity: O(N) – Traversing the remaining linked list.
- Space Complexity: O(1) – Used constant extra space.

## Approach 2: Optimized (O(1))

After analyzing the problem constraints, I realized that traversing the entire linked list was unnecessary.

Since the given node is guaranteed not to be the last node:

1. Copy the value of the next node into the given node.
2. Update the given node's `next` pointer to skip the next node.

**Complexity Analysis:**
- Time Complexity: O(1) – Only a constant number of operations.
- Space Complexity: O(1) – No additional data structures required.

## Key Learning

Initially, I used traversal to solve the problem in O(N) time. By analyzing the constraints more carefully, I optimized the solution to O(1) time.

**Takeaway:** Understanding problem constraints can help eliminate unnecessary operations and lead to more efficient solutions.