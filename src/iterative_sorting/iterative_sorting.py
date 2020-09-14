"""
Selection sort - O(n^2)

1. Current boundary start at 0
2. Find the smallest element in the array and move it to the front 
3. Swap the element to where we know it's supposed to go
4. Increment current boundry to 1 and repeat 
5. When current boundry > length(arr) - 1 return  the sorted array

Runtime Complexity:
    walking the boundry from one end to the other: O(n)
    finding the smallest element: O(n)
    total = O(n) * O(n) 
          = O(n^2)
"""

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        #current boundry starts at 0
        curr_bound = i
        #set smallest element to first element at the current boundry
        smallest_index = i
        #loop through rest of the array
        for j in range(curr_bound, len(arr)):
            #if find an element that is smaller than the element at the current smallest index
            if arr[j] < arr[smallest_index]:
                #swap the index 
                smallest_index = j
        #swap the current boundy with the smallest index 
        arr[curr_bound], arr[smallest_index] = arr[smallest_index], arr[curr_bound]
        
    return arr

"""
Bubble Sort - O(n^2)

1. Compare elements that are next to one another
2. If right element is less than left element swap elements 
3. Keep swapping until you go through array and don't need to swap any elements 
4. Return the sorted array
"""
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
