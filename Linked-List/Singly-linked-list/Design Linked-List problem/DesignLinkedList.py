# Problem: (707) Design Linked List
# Platform: Leetcode


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None  # Points to the first node

    def get(self, index: int) -> int:
        # Handle empty list and invalid index
        if(self.head is None or index < 0):
            return -1

        current = self.head
        count = 0

        # Traverse until the required index is reached
        while((count < index) and (current is not None)):
            count += 1
            current = current.next

        # Index is out of bounds
        if(current is None):
            return -1

        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if(self.head is None):
            self.head = new_node
            return

        # Link the new node to the current head
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if(self.head is None):
            self.head = new_node
            return

        current = self.head

        # Traverse to the last node
        while(current.next is not None):
            current = current.next

        # Attach the new node at the end
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        # Inserting at index 0 means inserting at the head
        if(index == 0):
            return self.addAtHead(val)

        # Handle empty list and negative index
        if(self.head is None or index < 0):
            return -1

        prev = None
        current = self.head
        count = 0

        # Traverse to the node currently present at the given index
        while((current is not None) and (count < index)):
            prev = current
            current = current.next
            count += 1

        # Index is greater than the current list length
        if(current is None and count < index):
            return

        # If current is None, index equals the list length.
        # Insert the new node at the tail.
        if(current is None):
            return self.addAtTail(val)

        # Insert the new node between prev and current
        prev.next = new_node
        new_node.next = current

    def deleteAtIndex(self, index: int) -> None:

        # Handle empty list
        if(self.head is None):
            return -1

        # Deleting index 0 means updating the head
        if(index == 0):
            self.head = self.head.next
            return

        prev = None
        current = self.head
        count = 0

        # Traverse to the node that needs to be deleted
        while((current is not None) and (count < index)):
            prev = current
            current = current.next
            count += 1

        # Index is out of bounds
        if(current is None):
            return -1

        # Skip the current node to remove it from the list
        prev.next = current.next

