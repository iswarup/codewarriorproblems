

'''Cyclically rotating all the elements of an array by one.

Input: [1,2,3,4,5,6,7,8] Output: [8,1,2,3,4,5,6,7]'''

arr = [1,2,3,4,5,6,7,8]

print([arr[-1]]+arr[:-1])