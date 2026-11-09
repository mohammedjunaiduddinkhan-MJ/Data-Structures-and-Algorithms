# Problem: Sum of elements of array
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/sum-all-array-elements/1

def arraySum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)