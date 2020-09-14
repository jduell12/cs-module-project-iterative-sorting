def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found

"""
Binary Search

1. Find the midpoint element 
    - round down if even elements 
2. Compare the target against the midpoint element 
3. If the target matches the midpoint element return the index 
4. Otherwise, determine which direction the binary search needs to go in
5. Repeat from Step 1 until find the target or if target not in array return -1 


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