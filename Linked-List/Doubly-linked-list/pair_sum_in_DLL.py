# Problem: Pair sum in Doubly linked list
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

def givenSumPairs(head, target):
        # code here
        if(not(head)):
            return []
        result = []
        left,right = head,head
        while (right.next is not None):
            right = right.next
        while(left.data < right.data):
            total_sum = left.data + right.data
            if(total_sum == target):
                result.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif(total_sum > target):
                right = right.prev
            else:
                left = left.next
        return result

# Time Complexity: O(n) + O(n) ~ O(n) 
# #First while loop is used to set the right pointer at the last node, so it takes O(n) time.In the worst case,the second loop will traverse from first node to till last node using left node or from last node to first node using right pointer, So even this takes O(n) time
# Auxiliary Space Complexity: O(1)