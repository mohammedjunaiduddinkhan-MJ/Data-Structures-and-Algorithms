### Approach: Floyd's Cycle Detection Algorithm (Tortoise and Hare)

This solution uses Floyd's Cycle Detection Algorithm to detect a cycle in a linked list and find its starting node.

**Phase 1: Cycle Detection**
- Initialize two pointers, `slow` and `fast`, at the head.
- Move `slow` one step and `fast` two steps at a time.
- If both pointers meet, a cycle exists.
- If the fast pointer reaches `None`, no cycle exists, so return `None`.

**Phase 2: Finding the Cycle's Starting Node**
- Reset the `slow` pointer to the head while keeping `fast` at the meeting point.
- Move both pointers one step at a time.
- The node where they meet again is the starting node of the cycle.

**Complexity Analysis:**
- Time Complexity: O(N)
- Space Complexity: O(1)

This approach detects and locates a cycle without using any additional data structures.