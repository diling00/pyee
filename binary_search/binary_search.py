'''
Given a ordered array of integers and a target integer, find the position of the target integer.
Remember the position is the zero-based index of target integer in the array.abs.

For example: given an array like [1, 3, 4, 8, 10, 20, 48, 50, 101]:

target number 1 has position 0 (index of the first element in the array),
target number 3 has position 1,
target number 20 has position 5,
target number 101 has position 8 (index of the last element in the array)

The idea is that:
1. You first locate the middle position of the array.
2. If the number at the middle of the array is equal to the target number, the position is found.
3. If the number at the middle of the array is less than the target number, now the first half of
   the array can be thrown away and you only need to searh the second half of the array.
4. If the number at the middle of the array is greater than the target number, now the second half
   of the array can be thrown away and you only need to search the first half.

the steps 1-4 above are repeated till the target number has been found, or all the numbers in the
array are thrown away (cannot find the number). 

Take the array above as an example [1, 3, 4, 8, 10, 20, 48, 50, 101], and we want to find the position
of 4. Here are the steps:

1. The number at the middle position of the original array is number 10 with position 4, and because 
   number 10 is greater than the target number 4, so we throw away the second half of the array 
   (including number 10), and the numbers left are [1, 3, 4, 8].
2. The number at the middle position of the array [1, 3, 4, 8] is number 3 (with position 1), since 
   there are even number of elements in this array (4 elements), we choose the number on the left of
   the middle position. Also because number 3 is less than the target number 4, we throw away the
   first half of the array including number 3, and the numbers left are [4, 8].
3. The number at the middle position of the array [4, 8] is number 4, and we found it! And we know the
   position of the target number 4 is 2 since we kept track of the position of the numbers left as we
   throw away numbers.

You can find more information about the binary search method at https://en.wikipedia.org/wiki/Binary_search_algorithm.
   
The function can be defined as follows:   
'''

# The function binary_search use the binary search method to search the position of a target number
# in a given array. It returns the position of the target number (see the above descritption of 
# binary search).
def binary_search(a, num):
    # write your own function to search the position of num.
    return 0 # need to fix the return value to the actual position.


a = [1, 3, 4, 8, 10, 20, 48, 50, 101]

print (binary_search(a, 4))  # this should output 2

print (binary_search(a, 1))  # this should output 0
print (binary_search(a, 3))  # this should output 1
print (binary_search(a, 20))  # this should output 5
print (binary_search(a, 101))  # this should output 8

