# Design Linked List – Singly Linked List

## Problem Description
Implement a singly linked list from scratch using Python. The linked list supports various operations such as retrieving, inserting, and deleting nodes at specific positions.

Each node contains:
- `val`: Stores the value of the node.
- `next`: Stores the reference to the next node.

## Implemented Operations

| Operation | Description |
|---|---|
| `get(index)` | Returns the value at the given index. Returns `-1` if the index is invalid. |
| `addAtHead(val)` | Inserts a new node at the beginning of the linked list. |
| `addAtTail(val)` | Inserts a new node at the end of the linked list. |
| `addAtIndex(index, val)` | Inserts a new node at the specified index. |
| `deleteAtIndex(index)` | Deletes the node at the specified index. |

## Approach
- Created a `Node` class to represent individual nodes.
- Maintained a `head` pointer to access the beginning of the linked list.
- Used pointer traversal to access nodes at specific positions.
- Updated `next` references to perform insertion and deletion without shifting elements.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| `get(index)` | O(N) |
| `addAtHead(val)` | O(1) |
| `addAtTail(val)` | O(N) |
| `addAtIndex(index, val)` | O(N) |
| `deleteAtIndex(index)` | O(N) |

**Space Complexity:** O(1) auxiliary space per operation.

## Concepts Practiced
- Singly Linked Lists
- Node Creation
- Pointer Manipulation
- Traversal
- Insertion and Deletion
- Handling Edge Cases

## Platform
LeetCode – Design Linked List
