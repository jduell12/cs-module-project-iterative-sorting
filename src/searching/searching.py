"""
Linear Search - O(log n)

1. Start from index 0 
2. Check if the element at the index is equal to the target value 
3. If the element at the index is equal return the index 
4. Otherwise go to next index. If next index is out of bounds return -1 

"""
def linear_search(arr, target):
    


    return -1   # not found


"""
Binary Search - O(log n)

1. Find the midpoint element 
    - round down if even elements 
2. Compare the target against the midpoint element 
3. If the target matches the midpoint element return the index 
4. Otherwise, determine which direction the binary search needs to go in
5. Repeat from Step 1 until find the target or if target not in array return -1 

Binary Search O(log n)
Inserting into BST O(log n)

Total Runtime complexity: O(log n * log n) = O (log^2 n)

Ex. 
[3, 4, 6, 16, 26, 28, 52, 55]
  0 1  2  3   4   5   6   7
target: 55

*Array in sorted order 
* go to middle index 
    - index 3 -> 16 
    - 16 < 55
    - only check array from index 4 to index 7
* array we care about is now [26, 28, 52, 55]
                              4    5   6   7
* go to middle index
    - index 5 -> 28 
    - 28 < 55
    - only check array from index 6 to index 7
* array we care about is now [52, 55]
                               0   1
* go to middle index
    - index 0 -> 52
    - 52 < 55 
    - only check array from index 7 to index 7
* array we care about is now [55]
                               0
* go to middle index 
    - index 7 -> 55
    - 55 === 55 
    - return index aka 7

"""
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #keep track of left and right edges
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        #find midpoint element 
        # length // 2 (integer division - no floats after division)
        midpoint = ((right + left) //2)
        #check if midpoint
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            #toss out the left side of the array by changing left variable
            # add 1 to midpoint since we know the midpoint is not the target so we don't need to include it
            left = midpoint + 1
        else:
            #toss out the right side of the array without including the midpoint element
            right = midpoint - 1 
            
    return -1  # not found

