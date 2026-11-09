# Problem: Check if array is sorted 
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

def isSorted(arr):
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            return False   
    return True

# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)