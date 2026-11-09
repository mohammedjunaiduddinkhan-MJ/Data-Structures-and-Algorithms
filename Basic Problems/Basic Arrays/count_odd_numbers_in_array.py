# Problem: Delete All Occurrences of a Given Key in a Doubly Linked List
# Platform: takeUforward
# Link: https://takeuforward.org/practice/dsa/count-of-odd-numbers-in-array

def countOdd(arr, n):
    count = 0
    for num in arr:
        if(num % 2 != 0):
            count += 1
    return count

# Time Complexity: O(n) — visits every element once.
# Auxiliary Space Complexity: O(1) — uses only one extra variable.